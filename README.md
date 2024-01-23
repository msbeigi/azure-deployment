[![Python 3.8](https://github.com/msbeigi/deployment-demo/actions/workflows/main.yml/badge.svg)](https://github.com/msbeigi/deployment-demo/actions/workflows/main.yml)
[![Azure CLI](https://img.shields.io/badge/Azure%20CLI-2.0-blue.svg)](https://docs.microsoft.com/en-us/cli/azure/)
[![Azure Container Registry](https://img.shields.io/badge/ACR-Container%20Registry-orange.svg)](https://azure.microsoft.com/en-us/services/container-registry/)
[![Azure Container Instances](https://img.shields.io/badge/ACI-Container%20Instances-green.svg)](https://azure.microsoft.com/en-us/services/container-instances/)

# deployment-demo

This command-line tool uses the Traveling Salesman Problem (TSP) to find the shortest distance to visit a list of cities. It leverages the Pandas library for data manipulation and the Geopy library for distance calculations as sample to perform deployment.

```
    make all
```
### response
```
curl -X 'POST' \
  'https://musical-tribble-979pw77v7543r5q-8007.app.github.dev/locaction?city=Houston' \
  -H 'accept: application/json' \
  -d ''
```

## To build container
```
    docker build .
    docker build -t <image_name>:<tag> .

    docker image ls
```

## To run container
```
    docker run -p 8007:8007 025dae2be507
```

## To run bash file
```bash
    bash invoke.sh Atlanta
```
Example Response:
```json
    {
        "name":"Phoenix",
        "long":-112.074141,
        "lat":33.4484367
    }
```
## Pushing image into Azure Container Registry (ACR)
For login to container registry the authenticatoin is available in the Azure Portal, navigate to your Azure Container Registry (e.g. fastapicontainer.azurecr.io in this case). Under the "Settings" menu, select "Access keys." You'll find two access keys.

```
# 1- Login to ACR
docker login fastapicontainer.azurecr.io
# 2-Build the Docker image  

docker build -t mydockerrepo/myapiimage:1.0

# 3-Tag the Docker image with the ACR repository information
docker tag mydockerrepo/myapiimage:1.0 fastapicontainer.azurecr.io/myapiimage:1.0

# 4- Push the Docker Image to Azure Container Registry (ACR)
docker push fastapicontainer.azurecr.io/myapiimage:1.0


```

## Creating an Azure Container Instance (ACI)
Thankfully, Microsoft provides us with predefined containers with common configurations, and an intuitive user interface to install additional features. We can easily replace the default container with a more fully-featured container by going to the VS Code Command Palette (Ctrl + Shift + P), and choosing “Codespaces: Add Development Container Configuration Files…”

To install the Azure CLI in codespace:
```
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

```

creating the container by az bash:

```
# 1- Login to 
az login --use-device-code

# 2- create ACI with specific values: az container create --resource-group <your-resource-group> --name <aci-name> --image <your-acr-name>.azurecr.io/<image-name>:<tag> --cpu 1 --memory 1.5Gi --registry-username <acr-username> --registry-password <acr-password> --dns-name-label <aci-dns-name>

az container create --resource-group deployment-demo --name geoapicity --image fastapicontainer.azurecr.io/fastapi-app:v1.0 --dns-name-label geoapicity --ports 8007 --protocol TCP

# User: "Registry name" under Accesskeys , Password:"Password1"

# To check the logs of the container instance
az container logs --resource-group deployment-demo --name geoapicity
```

## Exposing the ACI as an endpoint
This script (call_sample_appService.py) tests the FastAPI endpoint deployed on Azure Container Instances. It sends a POST request to the /locaction endpoint with a specified city parameter and prints the response.
```
python call_sample_appService.py "New York"
# Started..
# Calling endpoint location city 
# Arg is: New York
# Request was successful!
# Response JSON: {'name': 'New York', 'long': -74.0060152, 'lat': 40.7127281}
```