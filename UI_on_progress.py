import random
import pygame
import os
pygame.font.init()

WORDPOOL = ["tree","basket","apple","aeroplane"] # well list of all words that is randomly selected for the question
NUM_APPEAR = 2 # the number of letters that show up at the start of the game(idk man makes the game easier)
NUM_ATTEMPT = 3
WIN_TEXT = "Gotcha!!"
LOSE_TEXT = "YOU ARE HANGED!!!"

WIDTH,HEIGHT = 800,600
WHITE = (255,255,255)
BLACK = (0,0,0)
FPS = 60
high_streak = 0
font = pygame.font.SysFont('Courier',33)
bg = pygame.image.load(os.path.join('hangman.png'))
bg_toscale = pygame.transform.scale(bg,(WIDTH,HEIGHT))


SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman!")

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

def draw(puzzle,win,high_streak):

    SCREEN.fill(WHITE)
    SCREEN.blit(bg_toscale,(0,0))

    hm = ' '.join(puzzle)
    text = font.render(hm,1,BLACK)
    SCREEN.blit(text,(400,210))

    score = "Highest Streak: " + str(high_streak)
    score_txt = font.render(score,1,BLACK)
    SCREEN.blit(score_txt,(400,375))
    

    if win != 0:
        if win == 2: win_text = WIN_TEXT
        elif win == 1: win_text = LOSE_TEXT

        win_text_render = font.render(win_text,1,BLACK)
        SCREEN.blit(win_text_render,(400,500)) 

    pygame.display.update()
    
def main(high_streak):

    clock = pygame.time.Clock()
    run = True
    atem = 0
    ans,puzzle = intializer()
    a = '@'
    win = 0

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                a = pygame.key.name(event.key)
                atem += 1

        puzzle,bool = filler(ans,puzzle,a)
        
        if '_' not in puzzle:
            win = 2
            draw(puzzle,win,high_streak)
            pygame.time.delay(2000)
            run = False
            high_streak += 1

        elif atem == NUM_ATTEMPT:
            win = 1
            draw(puzzle,win,high_streak)
            pygame.time.delay(2000)
            run = False
            high_streak = 0


        draw(puzzle,win,high_streak)
    
    main(high_streak)


main(high_streak)

