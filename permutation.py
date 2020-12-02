M = []


def isASolution(m, x):
    return len(m) == x


def doPasswordResult(x, y, m=[]):
    global M
    if isASolution(m, x):
        M.append(m.copy())
    else:
        for i in range(1, y+1):
            m.append(i)
            doPasswordResult(x, y, m)
            m.pop()


def doLotteryResult(availableList, nItem, m=[]):
    global M
    if isASolution(m, nItem):
        M.append(m.copy())
    else:
        l = availableList.copy()
        for i in range(len(l)):
            m.append(l[i])
            copyL = l.copy()
            l.pop(i)
            doLotteryResult(l, nItem, m)
            m.pop()
            l = copyL
