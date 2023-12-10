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

