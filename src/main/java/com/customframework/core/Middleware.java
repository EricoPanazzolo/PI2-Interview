package com.customframework.core;

@FunctionalInterface
public interface Middleware {
  Response handle(Request req, Handler next);
}
