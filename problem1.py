number = 642
sumDigits = lambda num: sum(int(digit) for digit in str(num))
print(sumDigits(number))