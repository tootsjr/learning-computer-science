# input() = A function that prompts the user to enter data
#           Returns the enetered data as a string


name = input("What is your name?: ")
age = int(input("How old are you ?: "))

birthday = input("Is it your birthday? (yes or y): ")

if (
    birthday.lower() == "yes" or birthday.lower() == "y"
):  # A cleaner way to do the same thing would be to do if birthday.lower() in ("yes", "y"):
    print("Happy birthday !")
    age = age + 1

print(f"Hello {name} you are {age} years old !")
