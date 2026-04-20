def listCompareAccuracy(oglist, newlist):
    if len(newlist) > len(oglist):
        biglen = len(newlist)
        smalllen = len(oglist)
    else:
        biglen = len(oglist)
        smalllen = len(newlist)

    correct = 0
    for i in range(smalllen):
        if newlist[i] == oglist[i]:
            correct += 1

    return round(correct/biglen, 4)