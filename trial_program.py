import random

WORDPOOL = ["tree","basket","apple","aeroplane"] # well list of all words that is randomly selected for the question
NUM_APPEAR = 2 # the number of letters that show up at the start of the game(idk man makes the game easier)
NUM_ATTEMPT = 3

def intializer(): 
    word = random.choice(WORDPOOL)
    word_lst_ans = [i for i in word]
    word_lst = []
    num_list = [j for j in range(len(word_lst_ans))]
    lst_appear = []

    for i in range(0,NUM_APPEAR):
        n = random.choice(num_list)
        lst_appear.append(n)
        num_list.remove(n)

    for i in range(len(word_lst_ans)):
        if i in lst_appear: word_lst.append(word_lst_ans[i])
        else: word_lst.append('_')

    return word_lst_ans,word_lst

def filler(ans,puzzle,inp):
    temp = ans.copy()
    bool = False
    while inp in temp:
        n = temp.index(inp)
        puzzle[n] = inp
        temp[n] = 0
        bool = True
    return puzzle,bool

def main():
    print("-----WELCOME TO HANGMAN!!-----\n")
    print("Well ur puzzle is ...")
    atem = 0
    ans,puzzle = intializer()
    while '_' in puzzle:
        print(' '.join(puzzle),"\n")
        inp = input("Enter ur guess: ")
        print("\n")
        puzzle,bool = filler(ans,puzzle,inp)
        if bool: print("Ah! that s' a correct guess")
        else: print("Ah! fuck")
        print("\n")
        atem += 1
        if atem == NUM_ATTEMPT:
            print("Well u are Hanged son!!")
            break
    else:
        print(' '.join(puzzle))
        print('\nWell u live to fight a another day')

main()
