import random

def generate_id():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    
    id = ""
    
    for _ in range(3):
        id += random.choice(letters)
    
    for _ in range(3):
        id += random.choice(numbers)
    
    return id

print(generate_id())