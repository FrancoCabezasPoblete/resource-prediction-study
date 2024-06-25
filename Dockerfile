FROM python:3.10-slim-bullseye

COPY ./benchmarks /benchmarks
COPY ./src /src
COPY ./instances /instances

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    zlib1g-dev \
    lsb-release \
    wget \
    git \
    ltrace \
    strace \
    valgrind \
    time \
    && apt-get autoremove -y && apt-get clean -y

# Install OR-Tools for C++ (https://github.com/google/or-tools/releases/download/v9.9/or-tools_amd64_debian-11_cpp_v9.9.3963.tar.gz)
RUN wget https://github.com/google/or-tools/releases/download/v9.9/or-tools_amd64_debian-11_cpp_v9.9.3963.tar.gz -O /tmp/or-tools_amd64_debian-11_cpp_v9.9.3963.tar.gz \
    && mkdir -p /opt/ortools \
    && tar -xzvf /tmp/or-tools_amd64_debian-11_cpp_v9.9.3963.tar.gz -C /opt/ortools --strip-components=1 \
    && rm /tmp/or-tools_amd64_debian-11_cpp_v9.9.3963.tar.gz

ENV PATH="/opt/or-tools/bin:${PATH}"
ENV LD_LIBRARY_PATH="/opt/or-tools/lib:${LD_LIBRARY_PATH}"

RUN pip install --no-cache-dir -r /src/requirements.txt

RUN mkdir -p /benchmarks/build && cd /benchmarks/build && cmake .. && make
RUN mkdir /results

RUN chmod +x /benchmarks/run.sh 

ENTRYPOINT ["bash", "/benchmarks/run.sh"]