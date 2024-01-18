numbers = []
in_loop = True
while in_loop:
    number = int(input("Enter an integer: "))
    numbers.append(number) if number != 0 else 0
    in_loop = in_loop if number != 0 else False

print(max(numbers))