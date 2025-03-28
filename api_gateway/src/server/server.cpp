#include "server.h"

using namespace drogon;

HttpResponsePtr Server::buildResponse(ReqResult result,
                                      const HttpResponsePtr &resp) {
  auto clientResp = HttpResponse::newHttpResponse();
  if (result == ReqResult::Ok && resp) {
    clientResp->setStatusCode(resp->getStatusCode());
    clientResp->setBody(std::string(resp->getBody()));

    for (const auto &header : resp->headers()) {
      if (std::find(headers_to_skip_.begin(), headers_to_skip_.end(),
                    header.first) != headers_to_skip_.end()) {
        continue;
      }
      clientResp->addHeader(header.first, header.second);
    }

  } else {
    clientResp->setStatusCode(k500InternalServerError);
    clientResp->setBody("Error forwarding request");
  }
  return clientResp;
}

void Server::mainPageHandler(
    const HttpRequestPtr &req,
    std::function<void(const HttpResponsePtr &)> &&callback) {
  auto response = HttpResponse::newHttpResponse();
  response->setBody("Some main page response");
  callback(response);
}

void Server::userProxyHandler(
    const HttpRequestPtr &req,
    std::function<void(const HttpResponsePtr &)> &&callback,
    const std::string &path) {
  auto forwardedRequest = HttpRequest::newHttpRequest();
  forwardedRequest->setMethod(req->getMethod());

  std::string fullPath = "/v1/" + path;
  if (!req->query().empty()) {
    fullPath += "?" + req->query();
  }
  forwardedRequest->setPath(fullPath);

  forwardedRequest->setBody(std::string(req->getBody()));

  for (const auto &header : req->headers()) {
    if (std::find(headers_to_skip_.begin(), headers_to_skip_.end(),
                  header.first) != headers_to_skip_.end()) {
      continue;
    }
    forwardedRequest->addHeader(header.first, header.second);
  }

  user_service_->sendRequest(
      forwardedRequest,
      [this, callback](ReqResult result, const HttpResponsePtr &resp) {
        HttpResponsePtr response = buildResponse(result, resp);
        callback(response);
      });
}

void Server::start() {
  app().registerHandler(
      "/", [this](const HttpRequestPtr &req,
                  std::function<void(const HttpResponsePtr &)> &&callback) {
        mainPageHandler(req, std::move(callback));
      });

  app().registerHandler(
      "/v1/{path}",
      [this](const HttpRequestPtr &req,
             std::function<void(const HttpResponsePtr &)> &&callback,
             const std::string &path) {
        userProxyHandler(req, std::move(callback), path);
      });

  app().addListener("0.0.0.0", 8080).run();
}
