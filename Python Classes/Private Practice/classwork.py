english= float(input("english_str"))
english_str: str = input("Enter your english score: ")
chemistry = float(input("chemistry_str"))
chemistry_str: str = input("Enter your chemistry score: ")
physics = float(input("physics_str")) 
physics_str: str = input("Enter your physics score: ")
mathematics = float(input("mathematics_str"))
mathematics_str: str = input("Enter your mathematics score: ")
literature = float(input("literature_str"))
literature_str: str = input("Enter your literature score: ")

cgpa: float =(mathematics + english + chemistry + physics + literature) / 500
print("your CGPA is ") 