package com.customframework.core;

import java.util.List;

public class Route {
    private final String method;
    private final String path;
    private final Handler handler;
    private final List<Middleware> middlewares;

    public Route(String method, String path, Handler handler, List<Middleware> middlewares) {
        this.method = method;
        this.path = path;
        this.handler = handler;
        this.middlewares = middlewares;
    }

    public String getMethod() { return method; }
    public String getPath() { return path; }
    public Handler getHandler() { return handler; }
    public List<Middleware> getMiddlewares() { return middlewares; }
}
