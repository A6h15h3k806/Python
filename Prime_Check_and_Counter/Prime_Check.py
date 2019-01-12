def is_prime(x):
    p = True
    if x > 1:
        for i in range(2,x):
            if (x % i) == 0:
                p = False

    else:
       p = False
    
    print(p)

def main_module():
    def prime_check():
        y = int(input('''Enter the number you suspect is a prime:
'''))
        is_prime(y)

    prime_check()

    Terminator = input('''Press enter to start the module or 't' to terminate''')

    if Terminator == '' :
        while True:
            main_module()
    elif Terminator == 't' :
        print("Thank You and Good Bye !")
        quit()

    
Terminator = input('''Press enter to start the module or 't' to terminate''')

if Terminator == '' :
    main_module()
elif Terminator == 't' :
    print("Thank You and Good Bye !")
    quit()
