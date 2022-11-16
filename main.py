def N_factorial(num):
    if num <= 1:
        return 1
    else:
        return num * N_factorial(num - 1)

number = int(input('Enter a number: '))
fac = N_factorial(number)

print(f'factorialof {number} = {fac}')