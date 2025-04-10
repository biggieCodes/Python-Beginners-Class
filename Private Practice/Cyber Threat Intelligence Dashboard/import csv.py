import csv

filename = "data.csv"

# Open the file in write mode
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["Name", "Age", "City"])

    # Write data rows
    writer.writerow(["John", 25, "New York"])
    writer.writerow(["Alice", 30, "London"])
    writer.writerow(["Bob", 35, "Paris"])
