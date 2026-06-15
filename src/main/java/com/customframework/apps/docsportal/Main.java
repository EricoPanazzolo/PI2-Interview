package com.customframework.apps.docsportal;

import com.customframework.core.Router;
import com.customframework.core.Server;
import com.customframework.shared.StaticFileHandler;

public class Main {
  public static void main(String[] args) {
    Router router = new Router();
    router.addRoute("GET", "/", Controller::docsPortalHandler);
    router.addRoute(
        "GET",
        "/static/docs_portal.css",
        new StaticFileHandler(
            "/app/src/main/resources/apps/docs_portal/static", "docs_portal.css", "text/css"));
    Server.runServer(8082, router);
  }
}
