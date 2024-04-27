import random

responses = ["Yes.", "No.", "Ask again later.", "It is decidedly so.", "Outlook good.", "Outlook not so good."]

print(" __________")
print("|    __    |")
print("|   |__|   |")
print("|   |__|   |")
print("|__________|")
print("\nHello, I am pyball. Ask me any yes or no question, and I will answer it for you. If you want to exit, type 'pyball exit'.\n")
while True:
    user_input = input()

    if user_input == "pyball exit":
        quit()
    else:
        number = random.randint(0, 5)
        result = responses[number]
        print("\nresult\n")
    print("What's your next question?")

