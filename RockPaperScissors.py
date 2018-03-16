import random

options = ["Rock","Paper","Scissors"]
Computer = random.choice(options)
user = raw_input("Pick either Rock, Paper or Scissors: ")
user = user.lower()
if user == 'rock' or 'paper' or 'scissors':
    print "The computer has drawn %s whilst you have drawn %s " % (Computer,user)
if user == 'rock':
    if Computer == 'Rock':
        print 'Result=Tie Game'
    elif Computer == 'Paper':
        print 'Result=Computer Wins'
    else:
        print 'Result=User Wins'
if user == 'paper':
    if Computer == 'Rock':
        print 'Result=User Wins'
    elif Computer == 'Paper':
        print 'Result=Tie Game'
    else:
        print 'Result=Computer Wins'
if user == 'scissors':
    if Computer == 'Rock':
        print 'Result=Computer Wins'
    elif Computer == 'Paper':
        print 'Result=User Wins'
    else:
        print 'Result=Tie Game'
