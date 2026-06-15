package com.customframework.core;

import com.sun.net.httpserver.HttpExchange;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Utils {
  public static Request buildRequest(HttpExchange exchange) throws IOException {
    String method = exchange.getRequestMethod();
    String path = exchange.getRequestURI().getPath();

    // Parse query params
    Map<String, String> queryParams = new HashMap<>();
    String query = exchange.getRequestURI().getQuery();
    if (query != null) {
      for (String param : query.split("&")) {
        String[] entry = param.split("=", 2);
        try {
          if (entry.length > 1) {
            queryParams.put(
                URLDecoder.decode(entry[0], "UTF-8"), URLDecoder.decode(entry[1], "UTF-8"));
          } else {
            queryParams.put(URLDecoder.decode(entry[0], "UTF-8"), "");
          }
        } catch (UnsupportedEncodingException e) {
          // ignore
        }
      }
    }

    // Headers
    Map<String, String> headers = new HashMap<>();
    exchange
        .getRequestHeaders()
        .forEach(
            (k, v) -> {
              if (v != null && !v.isEmpty()) {
                headers.put(k, v.get(0));
              }
            });

    // Cookies
    Map<String, String> cookies = new HashMap<>();
    String cookieHeader = headers.get("Cookie");
    if (cookieHeader != null) {
      for (String cookie : cookieHeader.split(";")) {
        String[] entry = cookie.trim().split("=", 2);
        if (entry.length > 1) {
          cookies.put(entry[0], entry[1]);
        }
      }
    }

    // Body
    String body = "";
    if ("POST".equalsIgnoreCase(method)) {
      InputStream is = exchange.getRequestBody();
      ByteArrayOutputStream bos = new ByteArrayOutputStream();
      byte[] buffer = new byte[1024];
      int len;
      while ((len = is.read(buffer)) != -1) {
        bos.write(buffer, 0, len);
      }
      body = bos.toString("UTF-8");
    }

    return new Request(method, path, queryParams, headers, cookies, body);
  }

  public static void writeResponse(HttpExchange exchange, Response resp) throws IOException {
    // Add headers
    resp.getHeaders()
        .forEach(
            (k, values) -> {
              for (String v : values) {
                exchange.getResponseHeaders().add(k, v);
              }
            });

    // Ensure content type has charset if it's text
    String ct = resp.getContentType();
    if (ct != null) {
      if (ct.startsWith("text/") && !ct.contains("charset")) {
        ct += "; charset=utf-8";
      }
      exchange.getResponseHeaders().set("Content-Type", ct);
    }

    byte[] bodyBytes = resp.getBody() != null ? resp.getBody().getBytes("UTF-8") : new byte[0];

    // Send headers
    if (bodyBytes.length == 0) {
      exchange.sendResponseHeaders(resp.getStatusCode(), -1);
    } else {
      exchange.sendResponseHeaders(resp.getStatusCode(), bodyBytes.length);
    }

    if (bodyBytes.length > 0) {
      OutputStream os = exchange.getResponseBody();
      os.write(bodyBytes);
      os.close();
    } else {
      exchange.getResponseBody().close();
    }
  }

  public static String escapeHtml(String input) {
    if (input == null) return null;
    StringBuilder sb = new StringBuilder();
    for (char c : input.toCharArray()) {
      switch (c) {
        case '&':
          sb.append("&amp;");
          break;
        case '<':
          sb.append("&lt;");
          break;
        case '>':
          sb.append("&gt;");
          break;
        case '"':
          sb.append("&quot;");
          break;
        case '\'':
          sb.append("&#x27;");
          break;
        case '/':
          sb.append("&#x2F;");
          break;
        default:
          sb.append(c);
      }
    }
    return sb.toString();
  }

  public static Map<String, String> parseJson(String json) {
    Map<String, String> map = new HashMap<>();
    if (json == null || json.isEmpty()) return map;
    Pattern p = Pattern.compile("\"([^\"]+)\"\\s*:\\s*\"([^\"]+)\"");
    Matcher m = p.matcher(json);
    while (m.find()) {
      map.put(m.group(1), m.group(2));
    }
    return map;
  }
}
