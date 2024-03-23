import requests
import tkinter
from tkinter import *
from tkinter import messagebox
import smtplib

api_key = "989f8a4239a2223ddbef760cb7d966f8"
link = "https://api.openweathermap.org/data/2.5/weather?"

my_email = "shamaraj9342@gmail.com"
password = "jqqulqrnawqfntdx"


window = tkinter.Tk()
window.title("Weather Forecasting App")
window.config(padx=50, pady=50, background="#B1DDC6")


canvas = Canvas(width=800, height=526, background="#B1DDC6")
bg = PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=bg)

canvas.create_text(400, 50, text="Weather Forecasting App", fill="#B1DDC6", font=("Bernard Mt Condensed", 25, "bold"))
canvas.create_text(400, 150, text="This is the weather forecasting app for the User Desirable location", font=("Bernard Mt Condensed", 15))
canvas.grid(row=0, column=0)
canvas.config(highlightthickness=0)


email_label = canvas.create_text(330, 250, text="Email", font=("Bernard Mt Condensed", 20))
email_box = Entry()
email_box.place(x=380, y=240)
location_label = canvas.create_text(330, 350, text="Location", font=("Bernard Mt Condensed", 20))
location_box = Entry()
location_box.place(x=380, y=340)

def Search_weather():
    user_email = email_box.get()
    location_name = location_box.get()
    parameters = {
        "q": location_name,
        "appid": api_key,
        "units": "metric"
    }

    if len(location_name)==0:
        messagebox.showinfo("showinfo", "Please enter the location")


    response = requests.get(url=link, params=parameters)
    weather_data = response.json()
    weather_condition = weather_data["weather"][0]["id"]
    weather_description = weather_data["weather"][0]["description"]
    temperature_celsius = int(weather_data["main"]["temp"])


    if int(weather_condition) < 700:
        messagebox.showinfo("Current Weather", f"It can be rain today, take an umbrella with you")

    else:
        messagebox.showinfo("Current Weather", f"Today there is {weather_description} with {temperature_celsius}°c")

    weekly_message = messagebox.askquestion("Further Enquiry","Do you want to receive the weekly weather information?")
    weekly_weather_message = ""

    if weekly_message=="yes":
        response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
        weekly_data = response.json()

        for data in weekly_data["list"]:
            data_weekly = data["weather"][0]["id"]
            if int(data_weekly) < 700:
                weekly_weather_message = f"It can be rain on {data_weekly} day."
            else:
                weekly_weather_message = "The weather will be clear in the upcoming week."


        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=user_email, msg=weekly_weather_message)
        connection.close()

button_img = PhotoImage(file="button.png")
search_button = Button(text="Search", command=Search_weather)
search_button.place(x=360, y=440)



window.mainloop()