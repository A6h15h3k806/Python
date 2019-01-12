def Main_Module():
    u = int(input("Define uper limit: "))
    l = int(input("Define lower limit: "))
    list_p = []
    list_i = [i for i in range(l,u)]

    def is_prime(x):
        p = 1
        if x > 1:
            for i in range(2,x):
                if (x % i) == 0:
                    p = 0
        else:
            p = 0

        list_p.append(p)

    for s in range(l,u):
        is_prime(s)
    
    fav_out = list_p.count(1)

    poss_out = len(list_i)

    print(fav_out)
    print(poss_out)

    Terminator = input('''
Press 's' to start the module or 't' to terminate
''')
    if Terminator == 's':
        while True:
            Main_Module()
    
    elif Terminator == 't':
        print('''
Thank you and GoodBye!''')
        quit()

Terminator = input('''
Press 's' to start/restart the module otherwise press 't' to terminate 
''')

if Terminator == 's':
    Main_Module()
    
elif Terminator == 't':
    print('''
Thank you and GoodBye!''')
    quit()


