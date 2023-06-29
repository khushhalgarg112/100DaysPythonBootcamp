import requests
import datetime as dt
import smtplib

my_lati = 29.353861
my_long = 76.495880


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    data_set = response.json()
    latitide = float(data_set["iss_position"]["latitude"])
    longitude = float(data_set["iss_position"]["longitude"])
    if (
        my_lati - 5 <= latitide <= my_lati + 5
        and my_long - 5 <= longitude <= my_long + 5
    ):
        return True


def is_night():
    parameter = {
        "lat": my_lati,
        "lng": my_long,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time = dt.datetime.now().hour

    if time > sunset or time < sunrise:
        return True


if is_night() and is_iss_overhead():
    my_mail = "khusgarg1@gmail.com"
    password = "cykaddfeqswxekvz"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs="khusgarg2002@gmail.com",
            msg="Sunject: Look UP \n\n There is ISS above you",
        )
