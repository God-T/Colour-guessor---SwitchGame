from itertools import permutations, combinations


blue = u"\U0001F535"
red = u"\U0001F534"
green = u"\U0001F7E2"
yellow = u"\U0001f7e1"
pink = u"\U0001f7e3"
white = u"\u26AA"
colourBar = {'b': blue, 'r': red, 'g': green,
             'y': yellow, 'p': pink, 'w': white}
possibleResult = []

while(1):
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    inp = input('Enter guessed result?: ').split()
    # get selected balls:
    selectedBalls = [colourBar[c] for c in inp[0]]
    selectedBalls_dic = {i+1: selectedBalls[i] for i in range(4)}
    # get non-selected balls:
    nonSelectedBalls = [colourBar[key]
                        for key in colourBar if key not in inp[0]]

    redPinNo = int(inp[1])
    whitePinNo = int(inp[2])
    rightColourNo = redPinNo + whitePinNo
    rightPositionNo = redPinNo

    rightPositionBalls = [{}]
    if redPinNo > 0:
        comb = combinations(selectedBalls, rightPositionNo)
        rightPositionBalls = [{{selectedBalls[i]: i+1 for i in range(4)}[i]: i
                               for i in t} for t in comb]
    # print(rightPositionBalls, selectedBalls)
    tempRes = []
    for i in rightPositionBalls:
        otherEmptyPosition = [
            p for p in [1, 2, 3, 4] if p not in [c for c in i]]
        otherSelectedColours = [
            b for b in selectedBalls if b not in [i[c] for c in i]]
        comb = combinations(otherSelectedColours, whitePinNo)
        # print("]]]]]]", otherSelectedColours, otherEmptyPosition)

        if whitePinNo > 0:
            rightColourBalls = [[i for i in t] for t in comb]
            unknowBallNo = 4 - rightColourNo
            # guess the unshown ball colours
            if unknowBallNo > 0:
                comb = combinations(nonSelectedBalls, unknowBallNo)
                comb = [[c for c in t] for t in comb]
                newRightColourBalls = []
                for l in rightColourBalls:
                    newRightColourBalls += [l + bs for bs in comb]
                    # print(l, newRightColourBalls)
                    # [l + [c for c in t] for t in comb]
                    # print(l, [l + bs for bs in comb])
                rightColourBalls = newRightColourBalls
            perms = []
            for l in rightColourBalls:
                perm = permutations(l, len(otherEmptyPosition))
                perms += [{**{otherEmptyPosition[index]: t[index]
                              for index in range(len(t))}, **i} for t in perm]
            rightColourBalls = perms
        # print(">", selectedBalls_dic, i, otherEmptyPosition)
        # tempRes += rightColourBalls
        for l in rightColourBalls:
            Pass = True
            for key in l:
                if not i.get(key) and selectedBalls_dic[key] == l[key]:
                    Pass = False
                    break
            if Pass:
                tempRes += [l]

    # for li in tempRes:
    #     print("    ", li[1], li[2], li[3], li[4])

    if possibleResult == []:
        possibleResult = tempRes
    else:
        temp = []
        for dic in tempRes:
            if dic in possibleResult and dic not in temp and not dic == selectedBalls_dic:
                temp += [dic]
        possibleResult = temp
    # print("\nInput balls:", selectedBalls, " Red pins:",
    #       redPinNo, " white pins:", whitePinNo)

    for li in possibleResult:
        print("    ", li[1], li[2], li[3], li[4])
        #     print("    ", li)
