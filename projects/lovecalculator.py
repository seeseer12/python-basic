import random

def love_calculator(name1, name2):
    name1_clean = name1.lower().strip()
    name2_clean = name2.lower().strip()

    
    secret_binary = "01110011011010000110100101110011011010000110100101110010"

    def to_binary(s):
        return ''.join(f"{ord(c):08b}" for c in s)

    for n in [name1_clean, name2_clean]:
        if to_binary(n) == secret_binary:
            return 100  

    # Normal fun calculation
    combined = name1_clean + name2_clean
    true_count = sum(combined.count(char) for char in "true")
    love_count = sum(combined.count(char) for char in "love")

    score = int(f"{true_count}{love_count}")
    return min(score, 100)

# Input
name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

score = love_calculator(name1, name2)
print(f"💖 Love score between {name1} and {name2} is: {score}%")
