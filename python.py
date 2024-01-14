# Hangman Game
import random
    

play="True"

while play=="True":

    words=["Victory","Achievement","Mastery","Miracle","Accomplishment","Success","Triumph","Masterpiece","Joy","Bliss","Delight","Ecstasy","Elation","Jubilation","Zealous","Clever","Smart","Bright","Sharp","Brilliant","Intellectual"]
    for i in range(len(words)):
        word = random.choice(words)
    word=word.upper()

    l1 =len(word)
    print(l1)

    z=["-"]*l1
    l=0

    while(l<l1):
        guessWord=input()
        guessWord = guessWord.upper()
        
        if(guessWord in word):
            print("present")
            for i in range(0,l1):
                if(word[i]==guessWord):
                    print(guessWord)
                    z[i]=guessWord          
            print(z)

        if "-" not in z:
            print("\n\nHurray")
            print(f"You Did it! \tThe word is {word}")
            break
        
        l=l+1

    if "-" in z:
        print("Better Luck next Time")

    print("Do you want to continue?\nT or F")
    game=input()
    if(game=='T' or game =='t' or game=="y" or game=="Y" or game=='True' or game=='true' or game=='1'):
        play="True"
    else:
        play="False"

