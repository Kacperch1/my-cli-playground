temperature: float = float(input("whats the temperature today?"))
todaysTemperatoreMessage: str = "today is " + str(temperature) + " degree "
if temperature <= 0:
    print(todaysTemperatoreMessage +"you need warm clothes")
elif temperature <= 20:
    print(todaysTemperatoreMessage + "it's a nice temperature")
else:
    print(todaysTemperatoreMessage+ "it's very hot outside you should drink more water")

## TODO
## 1. Simplyfy message about temperature.
## 2. Do not repeat messages
## 3. Ask for yesterdays temperature in similar way u did for todays temperature
## 4. Simplify code as much as possible. Make it easy to work with.

##asking for yesterday temperature
temperature: int = float(input("What was yesterday's temperature? "))
temperaturemessage: str = "Yesterday was " + str(temperature) + " degree "

if temperature <= 0:
    print(temperaturemessage, "it was really cold")
elif temperature <= 20:
    print(temperaturemessage, "it was a nice temperature.")
else:
    print(temperaturemessage, "it was very hot, water was very important")