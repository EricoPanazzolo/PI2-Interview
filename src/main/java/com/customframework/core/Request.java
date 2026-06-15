package com.customframework.core;

import java.util.HashMap;
import java.util.Map;

public class Request {
  private final String method;
  private final String path;
  private final Map<String, String> queryParams;
  private final Map<String, String> headers;
  private final Map<String, String> cookies;
  private final String body;

  public Request(
      String method,
      String path,
      Map<String, String> queryParams,
      Map<String, String> headers,
      Map<String, String> cookies,
      String body) {
    this.method = method;
    this.path = path;
    this.queryParams = new HashMap<>(queryParams);
    this.headers = new HashMap<>(headers);
    this.cookies = new HashMap<>(cookies);
    this.body = body;
  }

  public String getMethod() {
    return method;
  }

  public String getPath() {
    return path;
  }

  public Map<String, String> getQueryParams() {
    return queryParams;
  }

  public Map<String, String> getHeaders() {
    return headers;
  }

  public Map<String, String> getCookies() {
    return cookies;
  }

  public String getBody() {
    return body;
  }

  public String getHeader(String name) {
    return getHeader(name, null);
  }

  public String getHeader(String name, String defaultValue) {
    if (headers == null) return defaultValue;
    for (Map.Entry<String, String> entry : headers.entrySet()) {
      if (entry.getKey().equalsIgnoreCase(name)) {
        return entry.getValue();
      }
    }
    return defaultValue;
  }
}
