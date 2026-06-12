package com.customframework.apps.buganizer;

import com.customframework.core.Router;
import com.customframework.core.Server;
import com.customframework.shared.StaticFileHandler;

public class Main {
    public static void main(String[] args) {
        Router router = new Router();
        router.addRoute("GET", "/", Controller::buganizerHandler);
        router.addRoute("GET", "/static/buganizer.css", new StaticFileHandler("/app/apps/buganizer/static", "buganizer.css", "text/css"));
        Server.runServer(8081, router);
    }
}
