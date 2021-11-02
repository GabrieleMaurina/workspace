print("Welcome to my calculator programme!")

while True:
    # try:
        operator = input("Enter a operator (+,-,* or /): ")
        num_1 = int(input("Enter the first number: "))
        num_2 = int(input("Enter the second number: "))
        q = input('Press Q to quit to the programme...')

        if operator == '+':
            print(num_1+num_2)
        elif operator == '-':
            print(num_1-num_2)
        elif operator == '*':
            print(num_1*num_2)
        elif operator == '/':
            print(num_1/num_2)
        elif q == 'q':
            break
