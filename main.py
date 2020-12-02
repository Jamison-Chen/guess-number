import answerMachine as am
import guessMachine as gm
target = am.prepareTarget()
print("Well, I'm prepared. Bet you can't get it right at once....")

playerBingo = False
playerTryTime = 0


while not playerBingo:
    playerTryTime += 1
    print("Please enter a 4-digit number without dupliate digits....")
    output = ""
    playerGuess = ""
    validInput = False
    # Wait for Player's Valid Guess
    while not validInput:
        validInput = True
        playerGuess = input()
        if len(playerGuess) != 4:
            validInput = False
        if not playerGuess.isdigit():
            validInput = False
        for each in playerGuess:
            if playerGuess.count(each) > 1:
                validInput = False
                break
        if validInput:
            break
        else:
            print("Please enter a 4-digit number without dupliate digits....")

    # Assess Player's Guess
    output = am.answer(target, playerGuess)
    if output == "4A0B":
        print("Impossible! You win!")
        playerBingo = True
    else:
        try:
            gm.playOnceWithHuman()
        except Exception:
            print("You lied! Get out!")
            break
        if gm.mes == "4A0B":
            print("Haha! You loser.")
            print("My number is: " + target)
            break
