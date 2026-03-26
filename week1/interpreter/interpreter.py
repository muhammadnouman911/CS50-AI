expression = input("Expression: ")

x, operator, y = expression.split(" ")

x, y = int(x), int(y)

result = None

match operator:
    case "+":
        result = x + y
    case "-":
        result = x - y
    case "*":
        result = x * y
    case "/":
        result = x / y if y != 0 else None

if result is not None:
    print(f"{result:.1f}")
