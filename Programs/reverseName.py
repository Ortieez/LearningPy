name = input("Enter your full name: ")

spl_name = name.split(" ")

for i in reversed(spl_name):
    print(i, end=" ")
