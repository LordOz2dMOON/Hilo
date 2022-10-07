import random
#class for hilo object
class Hilo:
    #method that instantiates the hilo gameh
    
  def game():
    score = 300
    while score != 0:
        current_card = x = int(random.randint(1, 13))
        next_card = x = int(random.randint(1, 13))
        print('The card is: ', current_card)
        user_feedback = input('Higher or lower? [h/l] ')
        print('Next card was: ', next_card)
        if user_feedback == 'l' and next_card < current_card:
            score += 100
            print('Your score is: ', score)
            continue_game = input('Play again? [y/n] ')
            if continue_game != 'n':
                continue
            else:
                break
        elif user_feedback == 'h' and next_card > current_card:
            score += 100
            print('Your score is: ', score)
            continue_game = input('Play again? [y/n] ')
            if continue_game != 'n':
                continue
            else:
                break
        elif user_feedback == 'l' and next_card > current_card:
            score -= 75
            print('Your score is: ', score)
            continue_game = input('Play again? [y/n] ')
            if continue_game != 'n':
                continue
            else:
                break
        elif user_feedback == 'h' and next_card < current_card:
            score -= 75
            print('Your score is: ', score)
            continue_game = input('Play again? [y/n] ')
            if continue_game != 'n':
                continue
            else:
                break
      
a = Hilo.game()