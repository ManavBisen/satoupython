import requests
import streamlit as st

st.title("Time to create API webapp")
st.header("This is a WebApp to see the weather")
city = st.text_input("Enter a city of your choice")

if city:
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=759e69376fce08b3bb8618e895467129"
  response = requests.get(url)

  weather_description = response.json()["weather"][0]["description"]
  temprature = response.json()["main"]["temp"]
  city_name = response.json()["name"]

  temp = temprature - 273.15
  if response.status_code == 200:
    st.write(f"Weather is {weather_description}")
    st.write(f"Temprature is {temp}")
    st.write(f"City name is {city_name}")

  elif response.status_code == 404:
    st.error("Invalid City")

  elif KeyError:
    st.error("Invalid City")

  elif "error" in weather_description or weather_description or temprature or city_name:
    st.error("Invalid City")
  
  elif response.status_code != 200:
    st.write("A newtwork error occured")

  else:
    st.write("Can't fetch weather information")

st.subheader("If you have time than you can read this:")
st.write("So... This is my first WebApp that I am hosting and also this is also one of my strating WebApps while I am a learner and that's also the reason that this page don't have a lot of things in it.")
st.write("One more thing is that my english isn't really good, so try to understand what I said.")
st.write("-- Satou")
st.subheader("GoodBye!")
