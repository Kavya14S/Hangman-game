import random
print("Let's play Hangman !")
print("You have only 6 lives so try to guess the word within 6 attempts! Good Luck !")
listt = ["apple","beautiful","moon","potato"]
word = random.choice(listt)
answer = ['_'] * len(word)
print(answer)
life = 6
while life!=0 and '_' in answer:
    guess = input("Guess a letter : ")
    guess = guess.lower()
    if guess in word :
        for i in range(len(word)):
            if word[i] == guess:
                answer[i] = guess
        print(answer)
    else:
        life-=1
if '_' in answer :
    print("You lose! The word was", word)
else :
    print("You won !")
