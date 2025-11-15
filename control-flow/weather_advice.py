#!/usr/bin/python3
current_weather = input("What's the weather like today? (sunny/rainy/cold):")

if current_weather is "sunny":
    print("Wear a t-shirt and sunglasses.")
elif current_weather is "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif current_weather is "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
