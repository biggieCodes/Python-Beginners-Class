full_name = input("Rabo Abdulsamad:")

name_length = len(full_name)

if name_length <= 10:
    print("Very short name")
elif name_length > 10 and name_length <= 20:
    print("Normal Name length")
else:
    print("Long name")