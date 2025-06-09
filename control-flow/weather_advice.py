User_response = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()
if User_response == "sunny":
    print("Wear a t-shirt and apply sunglasses.")
elif User_response == "rainy":
    print ("Don't forget your umbrella and a raincoat.")
elif User_response == "snowy":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

# This code provides weather-specific advice based on user input.

