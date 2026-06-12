package com.customframework.core;

import java.util.*;

public class Response {
  private String body;
  private int statusCode;
  private final Map<String, List<String>> headers = new LinkedHashMap<>();
  private String contentType;

  public Response(String body) {
    this(body, 200, "text/html");
  }

  public Response(String body, int statusCode) {
    this(body, statusCode, "text/html");
  }

  public Response(String body, String contentType) {
    this(body, 200, contentType);
  }

  public Response(String body, int statusCode, String contentType) {
    this.body = body;
    this.statusCode = statusCode;
    this.contentType = contentType;
    this.headers.put("Server", Collections.singletonList("LegacyEnterpriseServer/1.2"));
  }

  public void addHeader(String name, String value) {
    headers.computeIfAbsent(name, k -> new ArrayList<>()).add(value);
  }

  public void enableContentSecurityPolicy() {
    headers.put(
        "Content-Security-Policy",
        Collections.singletonList(
            "default-src 'none'; "
                + "script-src 'self' "
                + "'sha256-xIleX6e6xINtnrilaGBzRwSvTC0NFmz3D1ZMlmHa9No=' "
                + "'sha256-2FZsYC64EFt8wrUEi7hpJRiEmqKTDmyKgjmNoYfLS4o='; "
                + "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
                + "font-src https://fonts.gstatic.com; "
                + "connect-src 'self'; "
                + "form-action 'none'; "
                + "frame-ancestors 'none'; "
                + "base-uri 'none';"));
  }

  public void disableCaching() {
    headers.put(
        "Cache-Control",
        Collections.singletonList("no-store, no-cache, must-revalidate, max-age=0"));
    headers.put("Pragma", Collections.singletonList("no-cache"));
    headers.put("Expires", Collections.singletonList("0"));
  }

  public void enableHsts() {
    headers.put(
        "Strict-Transport-Security",
        Collections.singletonList("max-age=31536000; includeSubDomains"));
  }

  public void enableXssProtection() {
    headers.put("X-XSS-Protection", Collections.singletonList("1; mode=block"));
  }

  public void setReferrerPolicy(String policy) {
    headers.put("Referrer-Policy", Collections.singletonList(policy));
  }

  public void sanitize(String placeholder, String value) {
    if (this.body == null) return;
    String escapedValue = Utils.escapeHtml(value);
    String searchStr = "{{" + placeholder + "}}";
    this.body = this.body.replace(searchStr, escapedValue);
  }

  // Getters and Setters
  public String getBody() {
    return body;
  }

  public void setBody(String body) {
    this.body = body;
  }

  public int getStatusCode() {
    return statusCode;
  }

  public void setStatusCode(int statusCode) {
    this.statusCode = statusCode;
  }

  public void enableCors() {
    enableCors("*");
  }

  public void enableCors(String allowOrigin) {
    headers.put("Access-Control-Allow-Origin", Collections.singletonList(allowOrigin));
    headers.put(
        "Access-Control-Allow-Methods",
        Collections.singletonList("GET, POST, PUT, DELETE, OPTIONS"));
    headers.put(
        "Access-Control-Allow-Headers",
        Collections.singletonList("Content-Type, Authorization, X-Requested-With"));
  }

  public Map<String, List<String>> getHeaders() {
    return headers;
  }

  public String getContentType() {
    return contentType;
  }

  public void setContentType(String contentType) {
    this.contentType = contentType;
  }
}
