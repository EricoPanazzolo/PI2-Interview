package com.customframework.shared;

import com.customframework.core.Handler;
import com.customframework.core.Request;
import com.customframework.core.Response;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class StaticFileHandler implements Handler {
    private final String staticDir;
    private final String filename;
    private final String contentType;

    public StaticFileHandler(String staticDir, String filename, String contentType) {
        this.staticDir = staticDir;
        this.filename = filename;
        this.contentType = contentType;
    }

    @Override
    public Response handle(Request req) {
        java.nio.file.Path filePath = Paths.get(staticDir, filename);
        try {
            String content = new String(Files.readAllBytes(filePath), "UTF-8");
            return new Response(content, 200, contentType);
        } catch (IOException e) {
            return new Response("File not found", 404, "text/plain");
        }
    }
}
