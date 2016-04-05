#variables
#upper_bound = the highest value the person gives
#guess= the number the person guesses
#name =name of the person
#tries= the amount of times the person tries to get the answer

name = raw_input("What is your name?")
upper_bound = input("What is your highest value?")
tries = 0
guess = input("What number do you think it is?")
import random
answer = random.randint(0,upper_bound)
print answer
while guess!= answer:
    if guess > answer:
        print "Too high!"
    elif guess < answer:
        print "Too low"
    guess = input("What number do you think it is?")
    tries = tries +1
if tries==1:
    print name,"You got it right! It is",answer
else:
    print name,"it took you",tries,"tries."
