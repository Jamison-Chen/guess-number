import random
numberList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
tryTime = 0


def prepareTarget():
    return "".join(random.sample(numberList, 4))


def answer(targ, guess):
    global tryTime, bingo
    tryTime += 1
    outputMessage = ""

    countA = 0
    countB = 0
    for i in range(4):
        if targ.find(guess[i]) == i:
            countA += 1
        elif targ.find(guess[i]) != i and targ.find(guess[i]) != -1:
            countB += 1
    outputMessage = str(countA)+"A"+str(countB)+"B"
    if outputMessage != "4A0B":
        print("Wrong!("+outputMessage+")\nTime Used: " + str(tryTime))
        return outputMessage
    else:
        print("Bingo!!!!!("+outputMessage+")\nTime Used: " + str(tryTime))
        return outputMessage
