[![Python 3.8](https://github.com/msbeigi/deployment-demo/actions/workflows/main.yml/badge.svg)](https://github.com/msbeigi/deployment-demo/actions/workflows/main.yml)

# deployment-demo

This command-line tool uses the Traveling Salesman Problem (TSP) to find the shortest distance to visit a list of cities. It leverages the Pandas library for data manipulation and the Geopy library for distance calculations as sample to perform deployment.

```
    install -r requirements.txt
    make install
```

## To build container
```
    docker build .
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
## To push image into Azure container registry 

```
# 1- Login to ACR
docker login fastapicontainer.azurecr.io
# 2-Build the Docker image  

docker build -t mydockerrepo/myapiimage:1.0

# 1-Tag the Docker image with the ACR repository information
docker tag mydockerrepo/myapiimage:1.0 fastapicontainer.azurecr.io/myapiimage:1.0

# 4- Push the Docker Image to Azure Container Registry (ACR)
docker push fastapicontainer.azurecr.io/myapiimage:1.0


```
