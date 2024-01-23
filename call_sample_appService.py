import requests
import sys


def call_fastapi_app(city):
    url = f"http://geoapicity.eastus.azurecontainer.io:8007/locaction?city={city}"
    response = requests.post(url)

    if response.status_code == 200:
        print("Request was successful!")
        print("Response JSON:", response.json())
    else:
        print(f"Error: {response.status_code}")
        print("Response text:", response.text)



if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: python call_sample_appService.py <city>")
    #     sys.exit(1)


    print("Started..")
    city_arg = sys.argv[1]
    print('Calling endpoint location city \nArg is:', city_arg)
    call_fastapi_app(city_arg)

