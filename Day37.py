import requests
import datetime as dt

USER = "khushhalgarg"
TOKEN = "himangbender"
GRAPH_ID = "codegraph"
TODAY = f"{dt.datetime.now().year}0{dt.datetime.now().month}0{dt.datetime.now().day}"
pixels_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# responose = requests.post(url=pixels_endpoint, json=parameters)
# print(responose.text)

graph_endpoint = f"{pixels_endpoint}/{USER}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Code Time",
    "unit": "hour",
    "type": "float",
    "color": "ajisai",
}

headers_config = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers_config)
# print(response.text)

put_pixel_endpoints = f"{pixels_endpoint}/{USER}/graphs/{GRAPH_ID}"

put_pixel_config = {
    "date": TODAY,
    "quantity": input("How many hours you code today ?"),
}

response = requests.post(
    url=put_pixel_endpoints, json=put_pixel_config, headers=headers_config
)
print(response.text)

update_pixel_endpoint = f"{pixels_endpoint}/{USER}/graphs/{GRAPH_ID}/{TODAY}"

update_pixel_config = {
    "quantity": input("Update your coding hours"),
}
# response = requests.put(
#     url=update_pixel_endpoint, json=update_pixel_config, headers=headers_config
# )
# print(response.text)

response = requests.delete(url=update_pixel_endpoint, headers=headers_config)
print(response.text)
