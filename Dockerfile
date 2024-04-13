FROM ubuntu:22.04

# Install git and get the repository
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/FrancoCabezasPoblete/resource-prediction-study

# Set the working directory
WORKDIR /resource-prediction-study