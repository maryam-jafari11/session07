numbers = []

def num():
    numbers.append(x)
    return x




while True:
    x = input("enter your number or press C for break: ")
    if x == "C":
        break
    else:
        num()

sorted_numbers = sorted(numbers)
print(sorted_numbers)