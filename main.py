import random


def main():
    total = 0
    numbers = []
    
    while total <= 100:
        num = random.randint(1, 10)
        numbers.append(num)
        total += num

    print("Some of the random numbers (excluding the last one):")
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
