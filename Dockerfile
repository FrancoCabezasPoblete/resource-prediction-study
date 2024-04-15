FROM ubuntu:22.04

# Install git and get the repository
RUN apt-get update && apt-get install -y git linux-perf ltrace strace make g++
RUN git clone https://github.com/FrancoCabezasPoblete/resource-prediction-study
# Install python3
RUN apt-get install -y python3 python3-pip
# Install python dependencies
RUN pip3 install --no-cache-dir numpy icecream faker

# Set the working directory
WORKDIR /resource-prediction-study