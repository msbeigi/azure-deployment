import requests
import sys


def call_fastapi_app(city):
    url = "https://goesmaplepy.azurewebsites.net/location"

    # Data to be sent in the POST request
    data = {"city": city}

    # Sending a POST request to the FastAPI endpoint
    response = requests.post(url, json=data, timeout=10)

    # Check the status code of the response
    if response.status_code == 200:
        print("Request was successful!")
        print("Response JSON:", response.json())
    else:
        print(f"Error: {response.status_code}")
        print("Response text:", response.text)

# Replace "YourCityName" with the actual city you want to query
# call_fastapi_app("YourCityName")




if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python call_fastapi.py <city>")
        sys.exit(1)

    city_arg = sys.argv[1]

    call_fastapi_app(city_arg)