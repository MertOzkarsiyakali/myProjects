#Fahrenheit to Celcius Degree Converter by Countries


#Define the countries which use Fahrenheit
fahrenheit_countries = ["United States", "Liberia", "Belize", "Bahamas", "Micronesia", 
"Antigua And Barbuda", "Cayman Islands", "Bermuda", "Marshall Islands", "Saint Kitts And Nevis"
"Turks And Caicos Islands", "British Virgin Islands", "Palau", "Montserrat"]

#Define a function for converting Fahrenheit to Celcius degree
def fahrenheit_to_celcius(degree):
    #Use round for not get a complicated result
    return round( (degree - 32) / 1.8 )

#Define a function for converting Celcius to Fahrenheit degree    
def celcius_to_fahrenheit(degree):
    #Use round for not get a complicated result
    return round( (degree * 1.8) + 32 ) 

#Get location from user
location = input("Where are you now?(Type your country in English): ")    

#Testing for empty imput on location
if location:
    location = location.title()
else:
    #if it is empty raise a ValueError
    raise ValueError(" You should enter where you are ")

#Get value from user and convert to float for except calculation errors   
value = float(input("Enter your degree in local type: "))

#If input is empty raise a ValueError
if not value:
    raise ValueError("You should enter a value for conversion")

#Check for location is one of the Fahrenhait using countries
#If it is, use fahrenhait to celcius conversion         
if location in fahrenheit_countries:
    result = fahrenheit_to_celcius(value)
    print(f"Your degree (Fahrenheit) approximately equals to {result} Celcius degree")

#If the location is not one of the countries which use Fahrenhait, 
# then use Fahrenhait to Celcius conversion
else:
    result = celcius_to_fahrenheit(value)
    print(f"Your degree (Celcius) approximately equals to {result} Fahrenheit degree")
