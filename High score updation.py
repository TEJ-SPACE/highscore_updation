# The game() function in a program lets a user play a game and returns the score as an integer. 
# You need to read a file ‘High-score.txt’ which is either blank or contains the previous High-score. 
# You need to write a program to update the High-score 
# whenever the game() function breaks the High-score.

import random

def game():
    score = random.randint(1, 100)
    print("You are playing the game...")
    print(f"Your current high score is {score}: ")
    return score

with open("High-score.txt", "w") as f:
    output_list = [] # for code testing purposes
    score = game()
    high_score = 0
    count = 1
    while (high_score <= score or high_score >= score) and count != 11:
        if high_score > score:
            print(f"Score on try number {count} is: {high_score}")
            print("High score broken!")
            print(f"New high score: {high_score}\n")
            f.write(str(high_score))
            f.write("\n")
            output_list.append(high_score)
            score = high_score
            high_score = random.randint(1, 100)
            count += 1
        else:
            print(f"Score on try number {count} is: {high_score}")
            print("...Keep playing...\n")
            high_score = random.randint(1, 100)
            count += 1
print(output_list)



