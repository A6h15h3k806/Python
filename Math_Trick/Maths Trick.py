def Mathtrick():

    step1 = input('''
Think of a number but don't type it in just yet.
{Press enter to continue}
''')

    step2 = input('''Now add the same number to itself
{Press enter to continue}
''')

    import random

    for x in range(1):
            y = random.randint(1,50)*2

    step3 = input('''Now add %(y)i to your current number
{Press enter to continue}
''' % {"y":y})

    step4 = input('''Now divide your current number by 2
{Press enter to continue}
''')

    step5 = input('''Remember the number that you thought of in the beginning?
subtract that from your current number.
{Press enter to continue}
''')

    print('''Is your answer....

















''')

    print(y/2)

    Terminator = input('''
Press 's' to start/restart the module otherwise press 't' to terminate 
''') 

    if Terminator == 's':
        Mathtrick()
    
    elif Terminator == 't':
        print('''
Thank you and GoodBye!''')
        quit()

Terminator = input('''
Press 's' to start/restart the module otherwise press 't' to terminate 
''') 

if Terminator == 's':
    Mathtrick()
    
elif Terminator == 't':
    print('''
Thank you and GoodBye!''')
    quit()
