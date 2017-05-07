import random
colors = 'rybgop'

def codemaker():
    '''codemaker -> list
    generates code'''
    code = []
    for i in range(0,4):
        n = random.randint(0,5)     #chooses random integer
        code.append(colors[n])      #builds code randomly
    return code
def turn(guess, code):
    '''turn(userInput) -> list
    returns list of two numbers, number of blacks and number of whites'''
    guessResults = [0, 0]       #initialize list
    guessList = list(guess)
    if len(guessList) != 4:     #if guess is not 4 colors
        print('error! please input four-character guess')
        return False
    for i in range(0, 4):       
        l = guessList[i]
        if l not in colors:     #if guesss colors are not valid
            print('Error! Only colors possible are rybgop!')
            return False
        if l in code:
            if l == code[i]:     #if color is right color in right spot
                guessResults[0] += 1
            else:     #if color is right color not in right spot
                guessResults[1] += 1
    return guessResults
                
def mastermind():
    '''mastermind() -> none
    initializes game 
    '''
    while True:
        results = []
        code = codemaker()
        for i in range(0,10):
            print("I've got a quote of length 4. It uses colors in rybgop")
            guess = str(input("guess #"+str(i+1)+" -- enter your guess:"))
            results = turn(guess, code)     #results of guess
            if results[0] != 4:     #if guess is incorrect
                print(results[0],' black ',results[1],' white')          
            else:       #if guess is correct
                print("You Guessed the Code! Yay!")
                break
        if results[0] != 4:     #if player ran out of guesses
            print("You lost! Better Luck Next Time!")
        playAgain = str(input("Would you like to play another game? y or n:"))
        if playAgain == 'y':
            continue     #start new game
        elif playAgain == 'n':
            return False        #end game
        else:
            print("I'm sorry, I don't understand.")
            return False
            
