package com.customframework.apps.legacy;

import com.customframework.core.*;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

public class Controller {
  public static final String ADMIN_JWT_TOKEN =
      "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6ImFkbWluIn0.signature";
  public static final String GUEST_JWT_TOKEN =
      "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imd1ZXN0Iiwicm9sZSI6Imd1ZXN0In0.signature";

  private static final String APP_DIR = "/app/apps/legacy";
  private static final String TEMPLATE_DIR = APP_DIR + "/templates";

  private static String readTemplate(String filename) throws IOException {
    return new String(Files.readAllBytes(Paths.get(TEMPLATE_DIR, filename)), "UTF-8");
  }

  public static Response loginHandler(Request req) {
    try {
      String html = readTemplate("login.html");
      return new Response(html);
    } catch (IOException e) {
      return new Response("Template error", 500, "text/plain");
    }
  }

  public static Response authHandler(Request req) {
    if (req.getBody() == null || req.getBody().isEmpty()) {
      return new Response("{\"error\": \"Missing request body\"}", 400, "application/json");
    }

    Map<String, String> data = Utils.parseJson(req.getBody());
    String username = data.get("username");
    String password = data.get("password");

    if (username == null || password == null) {
      return new Response(
          "{\"error\": \"Username and password are required\"}", 400, "application/json");
    }

    if ("admin".equals(username) && "admin123".equals(password)) {
      String respPayload =
          String.format(
              "{\"authenticated\": true, \"token\": \"%s\", \"role\": \"administrator\"}",
              ADMIN_JWT_TOKEN);
      Response resp = new Response(respPayload, 200, "application/json");
      resp.addHeader("Set-Cookie", "auth_token=" + ADMIN_JWT_TOKEN + "; Path=/; HttpOnly");
      resp.addHeader("Set-Cookie", "role=admin; Path=/");
      return resp;
    } else {
      return new Response(
          "{\"authenticated\": false, \"error\": \"Invalid credentials\"}",
          401,
          "application/json");
    }
  }

  public static Response adminHomeHandler(Request req) {
    try {
      String html = readTemplate("admin_home.html");
      return new Response(html);
    } catch (IOException e) {
      return new Response("Template error", 500, "text/plain");
    }
  }

  public static Response profileHandler(Request req) {
    boolean isAdmin =
        "admin".equals(req.getCookies().get("role"))
            && ADMIN_JWT_TOKEN.equals(req.getCookies().get("auth_token"));
    boolean isGuest =
        "guest".equals(req.getCookies().get("role"))
            && GUEST_JWT_TOKEN.equals(req.getCookies().get("auth_token"));

    String profileParam = req.getQueryParams().get("name");
    boolean setGuestCookies = false;

    if (!isAdmin && !isGuest) {
      setGuestCookies = true;
      if (profileParam == null) {
        profileParam = "guest";
      }
    } else if (isAdmin) {
      if (profileParam == null) {
        profileParam = "admin";
      }
    } else if (isGuest) {
      if (profileParam == null) {
        profileParam = "guest";
      }
    }

    String profileParamCleaned = profileParam != null ? profileParam.replace("'", "") : "Guest";

    try {
      String html = readTemplate("legacy_profile.html");
      html = html.replace("{{username}}", profileParamCleaned);
      Response resp = new Response(html);

      String adminButtonHtml = "";
      if (isAdmin) {
        adminButtonHtml =
            "<p><a href=\"/admin_home\" style=\"display: inline-block; "
                + "background-color: #007bff; color: white; padding: 10px 15px; "
                + "text-decoration: none; border-radius: 4px; margin-top: 15px;\">"
                + "Go to Admin Dashboard</a></p>";
      }
      String body = resp.getBody().replace("{{admin_button}}", adminButtonHtml);
      resp.setBody(body);

      if (setGuestCookies) {
        resp.addHeader("Set-Cookie", "auth_token=" + GUEST_JWT_TOKEN + "; Path=/");
        resp.addHeader("Set-Cookie", "role=guest; Path=/");
      }
      return resp;
    } catch (IOException e) {
      return new Response("Template error", 500, "text/plain");
    }
  }

  public static Response homeHandler(Request req) {
    try {
      String html = readTemplate("index.html");
      return new Response(html);
    } catch (IOException e) {
      return new Response("Template error", 500, "text/plain");
    }
  }

  public static Response aboutHandler(Request req) {
    return new Response("<h1>About Us</h1><p>This is the Legacy Enterprise Portal.</p>");
  }

  public static Response contactHandler(Request req) {
    return new Response(
        "<h1>Contact Us</h1><p>Contact support at support@enterprise.example.com</p>");
  }

  public static Response statusHandler(Request req) {
    return new Response(
        "{\"status\": \"healthy\", \"service\": \"legacy-enterprise-portal\"}",
        200,
        "application/json");
  }

  public static Response usersHandler(Request req) {
    return new Response(
        "{\"users\": [{\"username\": \"admin\", \"role\": \"admin\"}, {\"username\": \"guest\","
            + " \"role\": \"guest\"}]}",
        200,
        "application/json");
  }

  public static Response settingsHandler(Request req) {
    return new Response("{\"settings\": {\"maintenance_mode\": false}}", 200, "application/json");
  }

  public static Response logoutHandler(Request req) {
    Response resp = new Response("", 302);
    resp.addHeader("Location", "/login");
    resp.addHeader("Set-Cookie", "auth_token=; Path=/; Max-Age=0");
    resp.addHeader("Set-Cookie", "role=; Path=/; Max-Age=0");
    return resp;
  }
}
