import requests
import datetime as dt

APP_ID = "bea46de2"
APP_KEY = "9ada0dc4ce356f4a1f9a455ead9f2d5b"

GENDER = "Male"
WEIGHT = "52"
HEIGHT = "167"
AGE = 20

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_details = input("Enter your today workout routine-> ")

nutrition_param = {
    "query": exercise_details,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

response = requests.post(url=nutrition_endpoint, json=nutrition_param, headers=headers)
data = response.json()

shettly_endpoint = (
    "https://api.sheety.co/0d6ba0e8677fd7a1363927f0ace9f977/workoutTrack/workouts"
)
# basic = ('khushhal', 'Khushal123@')

SHETLY_TOKEN = "jskdhfkjhskdjfhjksd"
bearer_headers = {
"Authorization": f"Bearer {SHETLY_TOKEN}"
}

date = dt.datetime.now()

for exercise in data["exercises"]:
    shetlle_paramters = {
        "workout": {
            "date": f"{date.day}/{date.month}/{date.year}",
            "time": f"{date.strftime('%X')}",
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

response2 = requests.post(url=shettly_endpoint, json=shetlle_paramters, headers=bearer_headers)
print(response2.text)
