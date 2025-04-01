#include "server/server.h"

int main(int argc, char **argv) {
  if (argc < 3) {
    throw std::runtime_error("Http user service and activities service host should be specified!");
  }
  Server server(argv[1], argv[2], "");
  server.start();
  return 0;
}
