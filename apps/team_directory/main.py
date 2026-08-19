from http.server import BaseHTTPRequestHandler
from http.server import ThreadingHTTPServer
import json
import os
import sys
from urllib.parse import parse_qs
from urllib.parse import urlparse

# Add app root to sys.path
APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(APP_DIR))
sys.path.insert(0, PROJECT_ROOT)

from apps.team_directory.controller import get_team_detail_json
from apps.team_directory.controller import get_teams_json
from apps.team_directory.controller import render_team_directory_html
from apps.team_directory.controller import resolve_ownership_json
from apps.team_directory.controller import search_teams_json


class TeamDirectoryHTTPHandler(BaseHTTPRequestHandler):

  def send_html(self, content: str, status: int = 200):
    body = content.encode('utf-8')
    self.send_response(status)
    self.send_header('Content-Type', 'text/html; charset=utf-8')
    self.send_header('Content-Length', str(len(body)))
    self.end_headers()
    self.wfile.write(body)

  def send_json(self, data, status: int = 200):
    body = json.dumps(data, indent=2).encode('utf-8')
    self.send_response(status)
    self.send_header('Content-Type', 'application/json; charset=utf-8')
    self.send_header('Content-Length', str(len(body)))
    self.end_headers()
    self.wfile.write(body)

  def send_css(self, filepath: str):
    if os.path.exists(filepath):
      with open(filepath, 'rb') as f:
        content = f.read()
      self.send_response(200)
      self.send_header('Content-Type', 'text/css; charset=utf-8')
      self.send_header('Content-Length', str(len(content)))
      self.end_headers()
      self.wfile.write(content)
    else:
      self.send_error(404, 'File Not Found')

  def do_GET(self):
    parsed = urlparse(self.path)
    path = parsed.path.rstrip('/') or '/'
    query_params = parse_qs(parsed.query)

    # Static CSS
    if path == '/static/team_directory.css':
      css_path = os.path.join(APP_DIR, 'static', 'team_directory.css')
      self.send_css(css_path)
      return

    # Team Directory HTML UI
    if path == '/':
      html_content = render_team_directory_html()
      self.send_html(html_content)
      return

    # REST APIs
    if path == '/api/teams':
      self.send_json(get_teams_json())
      return

    if path == '/api/teams/detail':
      team_id = query_params.get('id', [''])[0]
      self.send_json(get_team_detail_json(team_id))
      return

    if path == '/api/search':
      q = query_params.get('q', [''])[0]
      self.send_json(search_teams_json(q))
      return

    if path == '/api/ownership':
      target = query_params.get('path', [''])[0] or query_params.get(
          'endpoint', ['']
      )[0]
      self.send_json(resolve_ownership_json(target))
      return

    self.send_error(404, f'Endpoint {path} Not Found')


def main():
  port = 8082
  server_address = ('', port)
  httpd = ThreadingHTTPServer(server_address, TeamDirectoryHTTPHandler)
  print(f'[Team Directory Server] Listening on http://0.0.0.0:{port}')
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    httpd.server_close()


if __name__ == '__main__':
  main()
