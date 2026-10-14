from random import randint
import matplotlib.pyplot as plt
import numpy as np

passages = np.zeros(40)
hist = []
T = 1000000

case = 0
for t in range(T):
    de1 = randint(1, 6)
    de2 = randint(1, 6)
    case = (case + de1 + de2)%40
    passages[case] += 1
    hist.append(case)

    if case==30:
        case = 10
        passages[case] += 1
        hist.append(case)
    elif case==2 or case==17 or case==33:
        carte = randint(1, 16)
        if carte==1:
            case=0
            passages[case] += 1
            hist.append(case)
        elif carte==2:
            case=10
            passages[case] += 1
            hist.append(case)
        elif carte==3:
            case=1
            passages[case] += 1
            hist.append(case)
    elif case==7 or case==22 or case==36:
        carte = randint(1, 16)
        if carte==1:
            case=39
            passages[case] += 1
            hist.append(case)
        elif carte==2:
            case=0
            passages[case] += 1
            hist.append(case)
        elif carte==3:
            case=24
            passages[case] += 1
            hist.append(case)
        elif carte==4:
            case=10
            passages[case] += 1
            hist.append(case)
        elif carte==5:
            case=11
            passages[case] += 1
            hist.append(case)
        elif carte==6:
            case=15
            passages[case] += 1
            hist.append(case)
        elif carte==7:
            case=(case-3)%40
            passages[case] += 1
            hist.append(case)

plt.hist(hist, bins=40, color='grey')
plt.show()
