
import time


average_list = []
t0 = int(time.time())

def timefy(x):
    
    print ('''Your Expected Waiting Time is''')
    s = x%60
    print(str(s)+" sec")

    if x//60 >= 1:
        m = (x//60)%60
        print(str(m)+" min")

        if (x//60)//60 >=1:
            h = ((x//60)//60)%60
            print(str(h)+" hours")

        
    else:
        print(str(s)+" sec")

    
    
def mainmodule():

    t_n = input('''
Type in your Token Number
''')
    c_n = input('''
Type in the Counter Number
''')
    def HosptWaitTime():

        
        Token_Number = int(t_n)
        Counter_Number = int(c_n)
        N = Token_Number - Counter_Number 
        
        t00 = int(time.time())
        input('''
Press enter when the counter number changes
''')
        t1 = int(time.time())
        a = t1 - t00
        average_list.append(int(a))
        average = sum(average_list)/len(average_list)
        t3 = N * average
        t4 = t0 + t3
        t5 = int(time.time())
        t6 = t4 - t5
        timefy(int(t6))

        Terminator = input('''
Press enter to restart the module otherwise press 't' to terminate 
''') 

        if Terminator == '':
            HosptWaitTime()
    
        elif Terminator == 't':
            print('''
Thank you and GoodBye!''')
            quit()
    HosptWaitTime()
     
Terminator = input('''
Press 's' to start the module otherwise press 't' to terminate 
''')
if Terminator == 's':
    mainmodule()
    
elif Terminator == 't':
    print('''
Thank you and GoodBye!''')
    quit()


