import random
import time

# asking user how many dice they want to roll
dice_no=int(input("Enter the number of dice you want to roll: "))
print(f"Rolling {dice_no} dice...")
time.sleep(1)
print("The values are:")
for _ in range(dice_no):
    print(random.randint(1, 6))




# while(1):
#  a=input("Roll the dice? (yes/no): ")
#  if a.lower() == "yes":
#     print("Rolling the dice...")
#     print("The value is:", random.randint(1, 6))
#  elif a.lower() == "no":
#     print("Thanks for playing!")
#     break
#  else:
#     print("Invalid input. Please enter 'yes' or 'no'.")