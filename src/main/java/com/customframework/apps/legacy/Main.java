package com.customframework.apps.legacy;

import com.customframework.core.Router;
import com.customframework.core.Server;
import com.customframework.shared.StaticFileHandler;
import java.util.Collections;

public class Main {
  public static void main(String[] args) {
    Router router = new Router();

    // Register global middlewares
    router.use(Middlewares.adminCookieMiddleware);
    router.use(Middlewares.logMiddleware);
    router.use(Middlewares.securityHeadersMiddleware);

    // Register API Endpoints
    router.addRoute("GET", "/api/status", Controller::statusHandler);
    router.addRoute("POST", "/api/v1/auth", Controller::authHandler);
    router.addRoute("GET", "/api/v1/users", Controller::usersHandler);
    router.addRoute("GET", "/api/v1/settings", Controller::settingsHandler);

    // Register HTML Page Routes
    router.addRoute("GET", "/", Controller::homeHandler);
    router.addRoute("GET", "/home", Controller::homeHandler);
    router.addRoute("GET", "/about", Controller::aboutHandler);
    router.addRoute(
        "GET",
        "/contact",
        Controller::contactHandler,
        Collections.singletonList(Middlewares.logMiddleware));
    router.addRoute("GET", "/login", Controller::loginHandler);
    router.addRoute("GET", "/logout", Controller::logoutHandler);
    router.addRoute("GET", "/admin_home", Controller::adminHomeHandler);
    router.addRoute(
        "GET",
        "/profile",
        Controller::profileHandler,
        Collections.singletonList(Middlewares.referrerPolicyMiddleware));

    // Register Static Files
    String staticDir = "/app/src/main/resources/apps/legacy/static";
    router.addRoute(
        "GET", "/static/legacy.css", new StaticFileHandler(staticDir, "legacy.css", "text/css"));

    int port = 8080;
    Server.runServer(port, router);
  }
}
