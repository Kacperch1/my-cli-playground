name: str = input("whats your name: ")
lastname: str = input("whats your lastname: ")
age: int = input("whats your age : ")

full_name: str = name.capitalize() + " " + lastname.capitalize() +"!"
age_message: str = " You are " + str(age) + " years old."
print("Hello " + full_name + age_message)