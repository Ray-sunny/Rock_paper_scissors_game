import random
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
def get_result(gesture, num_com, your_scores, computer_scores, even_scores ,round):

    if gesture == 's' and num_com == 2:
        print('You win!')
        your_scores +=1
    elif gesture == 's' and num_com ==1:
        print('You lose')
        computer_scores +=1
    elif gesture == 'r' and num_com == 0:
        print('You win!')
        your_scores +=1
    elif gesture == 'r' and num_com ==2:
        print('You lose')
        computer_scores +=1
    elif gesture == 'p' and num_com ==1:
        print('You win!')
        your_scores += 1
    elif gesture == 'p' and num_com == 0:
        print('You lose')
        computer_scores +=1
    else:
        print('Even')
        even_scores +=1
    return your_scores, computer_scores, even_scores, round

round = 1
your_scores = 0
computer_scores = 0
even_scores = 0
continue_game = True
Round = 1
History = {}
win = 0
while  round < 4 or continue_game:
    gesture = input('please enter your gesture s(scissors) r(Rock) p(paper)').lower()

    if gesture not in ['s', 'r', 'p']:
        print('Please enter s or r or p and try again')
        continue
    if gesture =='s':
        print(f'your gesture:{scissor}')
    elif gesture == 'r':
        print(f'your gesture:{rock}')
    else:
        print(f'your gesture:{paper}')
    num_com = random.randint(0,2)
    if num_com == 0:
        print(f'computer gesture:{scissor}')
    elif num_com == 1:
        print(f'computer gesture:{rock}')
    else:
        print(f'computer gesture:{paper}')

    your_scores, computer_scores, even_scores, round = get_result(gesture, num_com, your_scores, computer_scores, even_scores, round)
    round += 1


    if round  == 4 :
        while True:
            answer = input(f'Do you want to play this game? yes or no').lower()
            if answer in ['yes', 'no']:
                break
            else:
                print('Please enter yes or no and try again')

        print(f'Your scores : {your_scores}, computer scores : {computer_scores} and even_scores : {even_scores}')
        if your_scores > computer_scores:
            win += 1
        History[Round] = (your_scores, computer_scores, even_scores)
        Round += 1
        if answer == 'yes':
            round = 1
            your_scores = 0
            computer_scores = 0
            even_scores = 0

        else:
            continue_game = False
            for i in range(0, Round-1):
                round_num = list(History.keys())[i]
                print(f'At Round{round_num}, Your scores: {History[round_num][0]}, Computer scores: {History[round_num][1]} and Even scores: {History[round_num][2]}')
            win_rate = win / (Round-1)
            win_rate_pre = "{:.2%}".format(win_rate)
            print(f'Your winning rate: {win_rate_pre}')

