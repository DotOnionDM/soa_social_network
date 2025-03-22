#pragma once

#include <drogon/HttpClient.h>
#include <drogon/HttpRequest.h>
#include <drogon/HttpResponse.h>
#include <drogon/drogon.h>

#include <set>

class Server {
public:
  Server() = delete;
  Server(const std::string &user_service, const std::string &activities_service,
         const std::string &statistics_service) {
    user_service_ = drogon::HttpClient::newHttpClient(user_service);
    activities_service_ = drogon::HttpClient::newHttpClient(activities_service);
    statistics_service_ = drogon::HttpClient::newHttpClient(statistics_service);
  }

  void start();

private:
  drogon::HttpClientPtr user_service_;
  drogon::HttpClientPtr activities_service_;
  drogon::HttpClientPtr statistics_service_;

  std::vector<std::string> headers_to_skip_ = {
      "content-length", "transfer-encoding", "host", "connection"};

  void mainPageHandler(
      const drogon::HttpRequestPtr &req,
      std::function<void(const drogon::HttpResponsePtr &)> &&callback);

  void userProxyHandler(
      const drogon::HttpRequestPtr &req,
      std::function<void(const drogon::HttpResponsePtr &)> &&callback,
      const std::string &path);

  drogon::HttpResponsePtr buildResponse(drogon::ReqResult result,
                                        const drogon::HttpResponsePtr &resp);
};
