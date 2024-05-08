FROM python:3.10-slim

COPY ./benchmarks /benchmarks
COPY ./src /src
COPY ./run_benchmarks.sh /run_benchmarks.sh

RUN apt-get update && apt-get install -y \
    git \
    ltrace \
    strace \
    make \
    g++ \
    valgrind \
    time \
    && apt-get autoremove -y \
    && apt-get clean -y
RUN pip install --no-cache-dir -r /src/requirements.txt

ENV SA_INSTANCES=/benchmarks/simulated_annealing/instancias

RUN chmod +x /run_benchmarks.sh
RUN cd /benchmarks/simulated_annealing && make

ENTRYPOINT ["bash","/run_benchmarks.sh"]