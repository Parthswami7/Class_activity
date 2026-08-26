import random 
def pick_ball_experiment():
    balls = ['Blue','Red','Green']
    result = random.choice(balls)
    pro = balls.count('Red')/len(balls)
    print("Probability of Picking Red Ball is:",pro)
    if result == 'Red':
        return 'Red ball was picked'
    else:
        return 'Beter luck next time'
res = pick_ball_experiment()
print(res)