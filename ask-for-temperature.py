temperature = float(input("whats the temperature today?"))
todaysTemperatoreMessage = "today is " + str(temperature) + " degree "
if temperature <= 0:
    print(todaysTemperatoreMessage +"you need warm clothes")
elif temperature <= 20:
    print(todaysTemperatoreMessage + "It's a nice temperature")
else:
    print(todaysTemperatoreMessage+ "it's very hot outside you should drink more water")

## TODO
## 1. Simplyfy message about temperature.
## 2. Do not repeat messages
## 3. Ask for yesterdays temperature in similar way u did for todays temperature
## 4. Simplify code as much as possible. Make it easy to work with.