cmake_minimum_required(VERSION 3.10)
project(ApiGateway)

set(CMAKE_CXX_STANDARD 17)

add_executable(app src/main.cpp src/server/server.cpp)
target_include_directories(app PRIVATE src/server)

find_package(Drogon CONFIG REQUIRED)
target_link_libraries(app PRIVATE Drogon::Drogon) 
