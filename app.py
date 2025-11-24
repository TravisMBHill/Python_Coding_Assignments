#welcome message to start
print("Welcome to my Lego set purchase tracker!")
Lego_sets = input("How many Lego sets have you purchased this year? ")
#Change to float for calculation
#put in try except block to catch non numeric inputs
try:
    Lego_sets = float(Lego_sets)
    total_spent = Lego_sets * 49.99
except ValueError:
    print("Please put a valid number for amount of Lego sets.")
    exit()
#Print total spent
print(f"This year you've spent an estimated ${total_spent:.2f} on Lego sets!")