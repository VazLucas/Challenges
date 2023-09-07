print("Welcome to Animal's Hotels game")
print('Your mission to alocate the guests:')
print('Dog can not be next to a cat')
print('Dog can not be next to a bone')
print('Cat can not be next to a rat.')
print('Rat can not be next to a cheese.')
print('Unavaible room already have a guest')
print('G – cat')
print('C – dog')
print('R – rat')
print('O – bone')
print('Q – cheese')
print('* - unavaible room')
print('- - avaiable room')
print('           ----------------(First stage)--------------       ')
print('           ----------------Good luck--------------       ')
print('first, alocate the cat and the rat')

print('[ * | * | - | G ]')
print('[ R | - | * | * ]')

rat = int(input('in what room you want to put the rat? '))
cat = int(input('in what room you want to put  cat? '))


if (rat == 6 and cat == 3):

    print('congrats, you made it!')

    print('            ----------------(stage 2)--------------       ')

    print('In this stage you must alocate a dog, a bone and another dog')

    print('[ - | * | * | * ]')
    print('[ * | C | - | - ]')

    dog1 = int(input('in what room you want to put the first dog? '))
    bone = int(input('in what room you want to put the bone? '))
    dog2 = int(input('in what room you want to put the second dog? '))

    if ((bone == 1 and dog1 == 7 and dog2 == 8) or (bone == 1 and dog1 == 8 and dog2 == 7)):
        print('congrats, you made it!')
        print('            ----------------(stage 3)--------------       ')
        print('Now your missions is to put a cat, a bone and a rat. ')

        print('[ - | * | * | * ]')
        print('[ - | G | - | * ]')

        cat = int(input('where do you want to put  cat? '))
        bone = int(input('where do you want to put bone? '))
        rat = int(input('and teh rat? '))

        if (rat == 1 and bone == 5 and cat == 7):
            print('                    congrats, you made it!            ')
            print('            ----------------(stage 4)--------------       ')

            print('Now your mission is to alocate two cheeses and a bone')
            print('[ - | - | - | * ]')
            print('[ * | R | * | * ]')

            cheese = int(input('where do you want to put the  first cheese? '))
            bone = int(input('wher do you want to put the bone? '))
            cheese2 = int(input('And the last cheese? '))

            if ((bone == 2 and cheese == 3 and cheese2 == 1) or (bone == 2 and cheese == 1 and cheese2 == 3)):
                print('------congrats, you won!------')
            else:
                print('GAME OVER!!')
        else:
            print('GAME OVER!!')
    else:
        print('GAME OVER!!')
else:
    print('GAME OVER!!')
