FROM ubuntu:22.04

# Install git and get the repository
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/FrancoCabezasPoblete/resource-prediction-study

# Set the working directory
WORKDIR /resource-prediction-study

# Install the requirements
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt