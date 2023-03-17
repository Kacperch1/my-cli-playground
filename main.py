'''
name = input("whats your name: ")
lastname = input("whats your lastname: ")
age = input("whats your age : ")
print("Hello " + name + " " + lastname + "! " + "you have " + str(age) + " years old")'''
print("What's the temperature :")
temperature = float(input())
if temperature <= 0:
    print("today is cold you need warm clothes")
elif temperature <= 20:
    print("It's a nice temperature today")
else:
    print("it's very hot outside you should drink more water")