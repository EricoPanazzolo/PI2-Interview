package com.customframework.core;

@FunctionalInterface
public interface Handler {
  Response handle(Request req);
}
