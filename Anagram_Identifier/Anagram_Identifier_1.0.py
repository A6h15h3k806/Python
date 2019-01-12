

def anagram():

    word1 = input('''
Type the first word or phase here!
''')

    word2 = input('''
Type the second word or phase here!
''')
    def findAnagrams(word1, word2):
        word1 = str(word1)
        word2 = str(word2)
        word1 = word1.replace(' ', '')
        word2 = word2.replace(' ', '')
        word1 = word1.replace('?', '')
        word2 = word2.replace('?', '')        
        word1 = word1.replace('!', '')
        word2 = word2.replace('!', '')
        word1 = word1.replace('.', '')
        word2 = word2.replace('.', '')        
        word1 = word1.replace("'", '')
        word2 = word2.replace("'", '')
        word1 = word1.replace('"', '')
        word2 = word2.replace('"', '')
        word1 = word1.replace(',', '')
        word2 = word2.replace(',', '')
        word1 = word1.replace(';', '')
        word2 = word2.replace(';', '')        
        word1 = word1.replace(':', '')
        word2 = word2.replace(':', '')
        word1 = word1.replace('(', '')
        word2 = word2.replace('(', '')
        word1 = word1.replace(')', '')
        word2 = word2.replace(')', '')
        word1 = word1.replace('[', '')
        word2 = word2.replace('[', '')
        word1 = word1.replace(']', '')
        word2 = word2.replace(']', '')
        word1 = word1.replace('{', '')
        word2 = word2.replace('{', '')
        word1 = word1.replace('}', '')
        word2 = word2.replace('}', '')
        word1 = word1.replace('&', '')
        word2 = word2.replace('&', '')


        abc = sorted(word1.upper())
        xyz = sorted(word2.upper())

        if abc == xyz:
            print('''
Indeed the Words/Phases are Anagrams of each other !
''')
        else:
            print('''
These are not the Anagrams of each other!
''')

    findAnagrams(word1, word2)

    Terminator = input('''
Press 's' to start/restart the module otherwise press 't' to terminate  
''')
    if Terminator == 's':
        while True:
            anagram()
    elif Terminator == 't':
        print('''
Thank you and GoodBye!''')
        quit()


Terminator = input('''
Press 's' to start/restart the module otherwise press 't' to terminate 
''') 

if Terminator == 's':
    anagram()
    
elif Terminator == 't':
    print('''
Thank you and GoodBye!''')
    quit()

    
