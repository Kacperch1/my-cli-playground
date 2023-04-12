temperature = float(input("What was yesterday's temperature? "))
temperaturemessage = "Yesterday was " + str(temperature) + " degree "

if temperature <= 0:
    print(temperaturemessage, "it was really cold")
elif temperature <= 20:
    print(temperaturemessage, "it was a nice temperature.")
else:
    print(temperaturemessage, "it was very hot, water was very important")