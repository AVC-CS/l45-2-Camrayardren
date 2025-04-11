import random


def main():
    total = 0
    numbers = []
    
    while True:
        num = random.randint(1, 10)
        if total + num > 100:
            numbers.append(num)  
            break
        numbers.append(num)
        total += num

    for n in numbers[:-1]:
        print(n)


    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
