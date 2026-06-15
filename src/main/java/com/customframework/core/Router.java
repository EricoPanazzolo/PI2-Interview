package com.customframework.core;

import java.io.PrintWriter;
import java.io.StringWriter;
import java.util.*;

public class Router {
  private final List<Route> routes = new ArrayList<>();
  private final List<Middleware> globalMiddlewares = new ArrayList<>();

  public void use(Middleware middleware) {
    globalMiddlewares.add(middleware);
  }

  public void addRoute(String method, String path, Handler handler) {
    addRoute(method, path, handler, Collections.emptyList());
  }

  public void addRoute(String method, String path, Handler handler, List<Middleware> middlewares) {
    routes.add(new Route(method, path, handler, middlewares));
  }

  public Response route(Request req) {
    Route match = findRoute(req.getMethod(), req.getPath());
    if (match == null) {
      return new Response("Not Found", 404, "text/plain");
    }

    List<Middleware> chain = new ArrayList<>(globalMiddlewares);
    chain.addAll(match.getMiddlewares());

    Handler pipeline = match.getHandler();
    for (int i = chain.size() - 1; i >= 0; i--) {
      final Middleware mw = chain.get(i);
      final Handler next = pipeline;
      pipeline = (r) -> mw.handle(r, next);
    }

    try {
      return pipeline.handle(req);
    } catch (Exception e) {
      StringWriter sw = new StringWriter();
      e.printStackTrace(new PrintWriter(sw));
      return new Response("Internal Server Error\n" + sw.toString(), 500, "text/plain");
    }
  }

  private Route findRoute(String method, String path) {
    for (Route r : routes) {
      if (r.getMethod().equalsIgnoreCase(method) && r.getPath().equals(path)) {
        return r;
      }
    }
    return null;
  }
}
