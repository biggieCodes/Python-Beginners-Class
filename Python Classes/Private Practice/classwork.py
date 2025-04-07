Mathematics = float(input("Enter your mathematics score:40")
English = float(input("Enter your English score: "))
Chemistry = float(input("Enter your Chemistry score: "))
physics = float(input("Enter your Physics score: "))
Physics = float(input("Enter your Physics score: "))
Literature = float(input("Enter your Literature score: "))

# Calculate CGPA
total = Mathematics + English + Chemistry + physics + Literature
number_of_subjects = 0
# Count only subjects with non-zero scores
for score in [Mathematics, English, Chemistry, physics, Literature]:
    if score > 0:
        number_of_subjects += 1
if number_of_subjects == 0:
    print("No subjects entered. CGPA cannot be calculated.")
else:
    cgpa = total / number_of_subjects
    print(f"Your CGPA is:{cgpa:.2f}")