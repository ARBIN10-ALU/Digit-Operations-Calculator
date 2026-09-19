print("This program is able to add, subtract or multiply each digit of the number you provide.")

n = int(input("Enter a integer number: "))
original = n

sum = 0
sub = 0
multi = 1

while n != 0:
    d = n % 10
    sum = sum + d
    sub = sub - d
    multi = multi * d
    n = n // 10

print(f"The sum of each digit of {original} is {sum}")
print(f"The subtraction of each digit of {original} is {sub}")
print(f"The multiplication of each digit of {original} is {multi}")