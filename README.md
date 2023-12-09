[![Python 3.8](https://github.com/msbeigi/deployment-demo/actions/workflows/main.yml/badge.svg)](https://github.com/msbeigi/deployment-demo/actions/workflows/main.yml)

# deployment-demo

This command-line tool uses the Traveling Salesman Problem (TSP) to find the shortest distance to visit a list of cities. It leverages the Pandas library for data manipulation and the Geopy library for distance calculations as sample to perform deployment.

```
    install -r requirements.txt
    make install
```

## To run
```bash
    curl -X POST "http://your-api-url/location" -H "Content-Type: application/json" -d '{"city": "New York"}'
```
Example Response:
```json
    {
    "name": "New York",
    "lat": 40.7128,
    "long": -74.0060
    }
```

Access the Swagger documentation by visiting http://your-api-url/docs in your browser.