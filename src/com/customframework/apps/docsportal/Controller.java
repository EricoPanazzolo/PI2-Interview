package com.customframework.apps.docsportal;

import com.customframework.core.Request;
import com.customframework.core.Response;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Controller {
    private static final String TEMPLATE_DIR = "/app/apps/docs_portal/templates";

    public static Response docsPortalHandler(Request req) {
        try {
            String html = new String(Files.readAllBytes(Paths.get(TEMPLATE_DIR, "docs_portal.html")), "UTF-8");
            return new Response(html);
        } catch (IOException e) {
            return new Response("Template error", 500, "text/plain");
        }
    }
}
