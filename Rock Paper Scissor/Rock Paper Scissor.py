import random,getpass
options = ['Rock','Paper','Scissor']
p1=p2=0
print("************************************************")
print("*                  Welcome                     *")
print("*        Let's Play Rocck Paper Scissor        *")
print("************************************************")
print("Choose from 'Rock','Paper','Scissor' only !!")
print("To stop playing hit 'end'")
while(True):
    first_choice = getpass.getpass('Chosse one Rock, Paper, Scissors : ', stream=None)
    if first_choice=='end':
        print('Score of player : ', p1)
        print('Score of Computer :', p2)
        if p1 > p2:
            print('Player Won by : ', p1 - p2, 'ponts !!!')
        elif p1 < p2:
            print('Computer Won by : ', p2 - p1, 'ponts !!!')
        else:
            print('Score Tied :', p1)
        break
    second_choice = random.choice(options)
    print('Computer Chooses :',second_choice)
    print('You Choose :',first_choice)
    if first_choice=='Rock' and second_choice=='Paper':
        print('Computer Won')
        p2+=1
        print('Score :',p1,':',p2)
    elif first_choice=='Rock' and second_choice=='Scissor':
        print('Player Won')
        p1+=1
        print('Score :', p1, ':', p2)
    elif first_choice=='Paper' and second_choice=='Scissor':
        print('Computer Won')
        p2 += 1
        print('Score :', p1, ':', p2)
    elif first_choice=='Paper' and second_choice=='Rock':
        print('Player Won')
        p1 += 1
        print('Score :', p1, ':', p2)
    elif first_choice=='Scissor' and second_choice=='Rock':
        print('Computer Won')
        p2 += 1
        print('Score :', p1, ':', p2)
    elif first_choice=='Scissor' and second_choice=='Paper':
        print('Player Won')
        p1 += 1
        print('Score :', p1, ':', p2)
    elif first_choice==second_choice:
        print('Same Strike , PLAY AGAIN !!!')