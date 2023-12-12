print('Smallest Factor of n and Prime numbers of range\nusing functions \nCreated by: Clyde Joshua C. Belongilot')
print('------------------------------------------------')

def factor():
    while True:
        var = eval(input("Enter Integer:"))
        if var < 2:
            print("Invalid input. Enter a number greater than or equal to 2.")
        elif var >= 2:
            for var2 in range(2, var):
                if var % var2 == 0:
                    print("Smallest factor other than 1 for", var, "is", var2)
                    break
        option = input("Do you want to continue calculating[y/n]?")
        
        if option.lower() != 'y':
            break

def prime_no():
    while True:
        start = eval(input("Enter a number [start]:"))
        if start < 0:
            print("Enter a non-negative number")

        elif start > 0:
            end = eval(input("Enter Integer [End]:"))

            if end < start:
                print("Enter a number greater than", start)

            elif end > start:
                print("Prime numbers between the range '",start ,"and",end, "are:")
                for prime in range(start, end + 1):

                    if prime > 1:

                        for i in range(2, prime):

                            if (prime % i) == 0:
                                break

                        else:
                            print(prime, end=' ')
        print()
        option2 = input("Continue calculating for prime numbers [y/n]?")
        if option2.lower() != 'y':
            break


while True:
    print("Enter [1] to find the smallest factor \nEnter [2] to find the prime numbers of range \nEnter [3] to terminate program")
    print("----------------------------------------")
    choice = int(input("Enter choice:"))

    if choice == 1:
        factor()

    elif choice == 2:
        prime_no()

    else:
        print("Program Terminated. Thank you for using!")
        print("-------------------------------------------")
        break

