user_list = []
while True:
    value = input("Enter a value: ")
    if value == "":
        break
    user_list.append(value)
print(f"Here's the list: {user_list}")