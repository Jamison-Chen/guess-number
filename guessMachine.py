import random
import permutation as p
import answerMachine as am
import time

# Algorithm here is not the best one.

numberList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
target = "".join(random.sample(numberList, 4))

numberListForComputerGuess = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
p.doLotteryResult(numberListForComputerGuess.copy(), 4)
possibleAnswer = p.M

cGHistroy = []
computerGuess = ""
mes = "5A5B"


def likelihood(l1, l2):
    samePlace = 0
    sameList = []
    for i in range(len(l1)):
        if l1[i] in l2:
            sameList.append(l1[i])
            if l2.index(l1[i]) == i:
                samePlace += 1
    return [len(sameList), sameList, samePlace]


def checkAll(l1, l2, AB):
    global cGHistroy
    i = 0
    while i < len(l1):
        if likelihood(l1[i], l2)[0] != (AB[0]+AB[1]):
            cGHistroy.append(l1[i])
            l1.pop(i)
        else:
            if likelihood(l1[i], l2)[2] != AB[0]:
                cGHistroy.append(l1[i])
                l1.pop(i)
            else:
                i += 1
    return l1


def guess(CG, message):
    global numberListForComputerGuess, possibleAnswer, cGHistroy
    A = int(message[0])
    B = int(message[2])
    if A == 0:
        if B == 0:
            for each in CG:
                numberListForComputerGuess.remove(each)
            p.M.clear()
            p.doLotteryResult(numberListForComputerGuess, 4)
            possibleAnswer = p.M
            for each in cGHistroy:
                try:
                    possibleAnswer.remove(each)
                except ValueError:
                    continue
            return "".join(possibleAnswer[0])
        elif B == 4:
            numberListForComputerGuess = list(CG)
            p.M.clear()
            p.doLotteryResult(numberListForComputerGuess, 4)
            possibleAnswer = p.M
            possibleAnswer = checkAll(possibleAnswer, list(CG), [A, B])
            for each in cGHistroy:
                try:
                    possibleAnswer.remove(each)
                except ValueError:
                    continue
            return "".join(possibleAnswer[0])
        else:
            possibleAnswer.remove(list(CG))
            possibleAnswer = checkAll(possibleAnswer, list(CG), [A, B])
            return "".join(possibleAnswer[0])
    elif A == 1:
        if B == 3:
            numberListForComputerGuess = list(CG)
            p.M.clear()
            p.doLotteryResult(numberListForComputerGuess, 4)
            possibleAnswer = p.M
            possibleAnswer = checkAll(possibleAnswer, list(CG), [A, B])
            for each in cGHistroy:
                try:
                    possibleAnswer.remove(each)
                except ValueError:
                    continue
            return "".join(possibleAnswer[0])
        else:
            possibleAnswer.remove(list(CG))
            possibleAnswer = checkAll(possibleAnswer, list(CG), [A, B])
            return "".join(possibleAnswer[0])
    elif A == 2:
        if B == 2:
            numberListForComputerGuess = list(CG)
            p.M.clear()
            p.doLotteryResult(numberListForComputerGuess, 4)
            possibleAnswer = p.M
            possibleAnswer = checkAll(possibleAnswer, list(CG), [A, B])
            for each in cGHistroy:
                try:
                    possibleAnswer.remove(each)
                except ValueError:
                    continue
            return "".join(possibleAnswer[0])
        else:
            possibleAnswer.remove(list(CG))
            possibleAnswer = checkAll(possibleAnswer, list(CG), [A, B])
            return "".join(possibleAnswer[0])
    elif A == 3:
        possibleAnswer.remove(list(CG))
        possibleAnswer = checkAll(possibleAnswer, list(CG), [A, B])
        return "".join(possibleAnswer[0])
    elif A == 5:
        return "".join(random.sample(numberList, 4))


def playUtilRight():
    global computerGuess, mes, cGHistroy
    computerBingo = False
    while not computerBingo:
        # time.sleep(1)
        computerGuess = guess(computerGuess, mes)
        cGHistroy.append(list(computerGuess))
        print("\t\t\t\t"+computerGuess)
        # time.sleep(1)
        mes = am.answer(target, computerGuess)
        # print(mes)
        if mes == "4A0B":
            computerBingo = True
            break


def playOnceWithHuman():
    global computerGuess, mes, cGHistroy
    # time.sleep(1)
    computerGuess = guess(computerGuess, mes)
    cGHistroy.append(list(computerGuess))
    print("\t\t\t\t"+computerGuess)
    # time.sleep(1)
    mes = input()
# playUtilRight()
