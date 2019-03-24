color = 'blue'
guess = ''
guesses = 0
#make sure not to put print twice or it will print the statment twice even
#if not needed
while guess != color:
    guess = input('What color am I thinking of? ')
    guesses = guesses + 1
print('You got it! It took you' , guesses , 'guesses')
 #make sure you use the variable name not the actual variable ie 'blue' or it
    #won't work

