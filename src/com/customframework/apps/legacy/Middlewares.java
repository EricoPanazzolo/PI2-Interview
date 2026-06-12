package com.customframework.apps.legacy;

import com.customframework.core.*;
import java.util.UUID;

public class Middlewares {
    public static final Middleware adminCookieMiddleware = (req, next) -> {
        boolean isAdmin = "admin".equals(req.getCookies().get("role")) &&
                          Controller.ADMIN_JWT_TOKEN.equals(req.getCookies().get("auth_token"));
        
        String path = req.getPath();
        if (path.startsWith("/admin_home") || path.startsWith("/api/v1/users") || path.startsWith("/api/v1/settings")) {
            if (!isAdmin) {
                if (path.startsWith("/api/")) {
                    return new Response("{\"error\": \"Forbidden\"}", 403, "application/json");
                } else {
                    Response resp = new Response("", 302);
                    resp.addHeader("Location", "/login");
                    return resp;
                }
            }
        }
        
        if ("/login".equals(path) && isAdmin) {
            Response resp = new Response("", 302);
            resp.addHeader("Location", "/admin_home");
            return resp;
        }
        
        return next.handle(req);
    };

    public static final Middleware globalSanitizerMiddleware = (req, next) -> {
        if (req.getQueryParams() != null) {
            req.getQueryParams().replaceAll((k, v) -> Utils.escapeHtml(v));
        }
        return next.handle(req);
    };

    public static final Middleware requestIdMiddleware = (req, next) -> {
        String requestId = UUID.randomUUID().toString();
        req.getHeaders().put("X-Request-ID", requestId);
        Response resp = next.handle(req);
        resp.addHeader("X-Request-ID", requestId);
        return resp;
    };

    public static final Middleware logMiddleware = (req, next) -> {
        long start = System.currentTimeMillis();
        String userAgent = req.getHeaders().getOrDefault("User-Agent", "Unknown");
        Logger.log(String.format("Routing Request: %s %s | Agent: %s", req.getMethod(), req.getPath(), userAgent));
        
        Response resp = next.handle(req);
        
        long duration = System.currentTimeMillis() - start;
        Logger.log(String.format("Response Status: %d | Time: %d ms | Type: %s", 
            resp.getStatusCode(), duration, resp.getContentType()));
        return resp;
    };

    public static final Middleware securityHeadersMiddleware = (req, next) -> {
        Response resp = next.handle(req);
        resp.enableXssProtection();
        resp.addHeader("X-Content-Type-Options", "nosniff");
        resp.addHeader("X-Frame-Options", "DENY");
        return resp;
    };

    public static final Middleware referrerPolicyMiddleware = (req, next) -> {
        Response resp = next.handle(req);
        resp.setReferrerPolicy("strict-origin-when-cross-origin");
        return resp;
    };
}
