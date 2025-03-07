#include "server/server.h"

int main(int argc, char **argv) {
  if (argc < 2) {
    throw std::runtime_error("Http user service host should be specified!");
  }
  Server server(argv[1], "", "");
  server.start();
  return 0;
}
