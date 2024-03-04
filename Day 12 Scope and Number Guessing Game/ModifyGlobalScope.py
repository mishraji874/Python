enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")