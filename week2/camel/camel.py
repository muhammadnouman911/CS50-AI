camel = input("camelCase: ")
snake = []

for char in camel:
    if char.isupper():
        snake.append("_")
    snake.append(char.lower())

snake = "".join(snake)

print(f"snake_case: {snake}")
