from http.server import BaseHTTPRequestHandler
from http.server import ThreadingHTTPServer
import json
import os
import sys
from urllib.parse import parse_qs
from urllib.parse import unquote
from urllib.parse import urlparse

# Add app root to sys.path
APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(APP_DIR))
sys.path.insert(0, PROJECT_ROOT)

from apps.buganizer.controller import add_comment_to_issue
from apps.buganizer.controller import assign_issue
from apps.buganizer.controller import get_all_issues_json
from apps.buganizer.controller import get_hotlist_json
from apps.buganizer.controller import get_issue_json
from apps.buganizer.controller import render_hotlist_html
from apps.buganizer.controller import render_issue_html


class BuganizerHTTPHandler(BaseHTTPRequestHandler):

  def send_html(self, content: str, status: int = 200):
    body = content.encode("utf-8")
    self.send_response(status)
    self.send_header("Content-Type", "text/html; charset=utf-8")
    self.send_header("Content-Length", str(len(body)))
    self.end_headers()
    self.wfile.write(body)

  def send_json(self, data, status: int = 200):
    body = json.dumps(data, indent=2).encode("utf-8")
    self.send_response(status)
    self.send_header("Content-Type", "application/json; charset=utf-8")
    self.send_header("Content-Length", str(len(body)))
    self.end_headers()
    self.wfile.write(body)

  def send_css(self, filepath: str):
    if os.path.exists(filepath):
      with open(filepath, "rb") as f:
        content = f.read()
      self.send_response(200)
      self.send_header("Content-Type", "text/css; charset=utf-8")
      self.send_header("Content-Length", str(len(content)))
      self.end_headers()
      self.wfile.write(content)
    else:
      self.send_error(404, "File Not Found")

  def do_GET(self):
    parsed = urlparse(self.path)
    path = parsed.path.rstrip("/") or "/"
    query_params = parse_qs(parsed.query)
    q = query_params.get("q", [""])[0] or query_params.get("search", [""])[0]

    # Static CSS
    if path == "/static/buganizer.css":
      css_path = os.path.join(APP_DIR, "static", "buganizer.css")
      self.send_css(css_path)
      return

    # Hotlist Views
    if path in (
        "/",
        "/hotlist",
        "/hotlists",
        "/hotlists/security-triage-queue",
        "/hotlists/5829104",
    ):
      html_content = render_hotlist_html("5829104", q)
      self.send_html(html_content)
      return

    if path in (
        "/hotlists/vulnerability-backlog",
        "/hotlists/7920155",
        "/search",
    ):
      html_content = render_hotlist_html("7920155", q)
      self.send_html(html_content)
      return

    # Bug Detail Views
    if path.startswith("/issues/"):
      issue_id = path.replace("/issues/", "").strip()
      html_content = render_issue_html(issue_id)
      self.send_html(html_content)
      return

    # REST APIs
    if path in ("/api/hotlists/5829104", "/api/hotlists/security-triage-queue"):
      self.send_json(get_hotlist_json("5829104", q))
      return

    if path in ("/api/hotlists/7920155", "/api/hotlists/vulnerability-backlog"):
      self.send_json(get_hotlist_json("7920155", q))
      return

    if path in ("/api/issues", "/api/search"):
      self.send_json(get_all_issues_json(q))
      return

    if path.startswith("/api/issues/"):
      issue_id = path.replace("/api/issues/", "").strip()
      self.send_json(get_issue_json(issue_id))
      return

    self.send_error(404, f"Endpoint {path} Not Found")

  def do_POST(self):
    parsed = urlparse(self.path)
    path = parsed.path.rstrip("/")

    length = int(self.headers.get("Content-Length", 0))
    raw_body = self.rfile.read(length) if length > 0 else b"{}"
    try:
      data = json.loads(raw_body.decode("utf-8"))
    except Exception:
      data = {}

    if path.startswith("/api/issues/") and path.endswith("/comments"):
      issue_id = path.replace("/api/issues/", "").replace("/comments", "").strip()
      res = add_comment_to_issue(
          issue_id,
          data.get("author"),
          data.get("text", ""),
          data.get("is_internal", True),
      )
      self.send_json(res)
      return

    if path.startswith("/api/issues/") and path.endswith("/assign"):
      issue_id = path.replace("/api/issues/", "").replace("/assign", "").strip()
      res = assign_issue(issue_id, data.get("assignee_ldap", ""))
      self.send_json(res)
      return

    self.send_error(404, f"POST Endpoint {path} Not Found")


def main():
  port = 8081
  server_address = ("", port)
  httpd = ThreadingHTTPServer(server_address, BuganizerHTTPHandler)
  print(f"[Buganizer Server] Listening on http://0.0.0.0:{port}")
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    httpd.server_close()


if __name__ == "__main__":
  main()
