FROM ubuntu:22.04

RUN apt update && apt install -y \
    build-essential \
    cmake \
    git \
    libjsoncpp-dev \
    uuid-dev \
    zlib1g-dev \
    libssl-dev

RUN apt install -y \ 
    curl \
    pkg-config \
    libbrotli-dev \
    libboost-all-dev \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/drogonframework/drogon.git && \
    cd drogon && \
    git submodule update --init && \
    mkdir build && \
    cd build && \
    cmake .. -DCMAKE_BUILD_TYPE=Release && \
    make -j$(nproc) && \
    make install && \
    ldconfig

COPY . app

WORKDIR /app

RUN mkdir -p build && cd build && \
    cmake .. && \
    make

EXPOSE 8080

CMD [ "./build/app", "http://user_service:8081" ]
