# Simple CGPA Calculator

# Ask for scores
math = float(input("Enter your Mathematics score:40 "))
english = float(input("Enter your English score:80 "))
chemistry = float(input("Enter your Chemistry score:90 "))
physics = float(input("Enter your Physics score:30 "))
literature = float(input("Enter your Literature score:0 "))

# Calculate CGPA
total = math + english + chemistry + physics + literature
number_of_subjects = 0

# Count only subjects with non-zero scores
for score in [math, english, chemistry, physics, literature]:
    if score > 0:
        number_of_subjects += 1

if number_of_subjects == 0:
    print("No subjects entered. CGPA cannot be calculated.")
else:
    cgpa = total / number_of_subjects
    print(f"Your CGPA is:{cgpa:.2f}")

