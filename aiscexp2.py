import pandas as pd
import random
bestAvg = 0
crossoverIdx = 3
mutationIdx = 4


def crossover(p1, p2):
    global crossoverIdx
    p1 = str(p1)
    p2 = str(p2)
    t1 = p1[:crossoverIdx]+p2[crossoverIdx:]
    t2 = p2[:crossoverIdx]+p1[crossoverIdx:]
    crossoverIdx = random.randint(0, 4)
    return [t1, t2]


def mutation(p1, p2):
    global mutationIdx
    p1 = str(p1)
    p2 = str(p2)

    def replace(x):
        return "1" if x == "0" else "0"
    p1 = list(p1)
    p1[mutationIdx] = replace(p1[mutationIdx])
    p1 = "".join(p1)

    p2 = list(p2)
    p2[mutationIdx] = replace(p2[mutationIdx])
    # print(p2)
    p2 = "".join(p2)
    mutationIdx = random.randint(0, 4)

    return [p1, p2]

def customFun(x):
    return 9*x +pow(x, 3)

def display(msg, data,bol=True):
    df = pd.DataFrame(data)
    if bol:
        print(msg)
    print(df)


x = [random.randint(0, 31) for i in range(4)]
fx = [customFun(i) for i in x]
pl = [((bin(i)[2:]).zfill(5)) for i in x]
pr = [i/sum(fx) for i in fx]
ec = [i/(sum(fx)/len(fx)) for i in fx]
ac = [round(i) for i in ec]
bestAvg = max(bestAvg, (sum(fx)/len(fx)))
data = {"x": x,    "f(x)": fx,    "parent": pl,    "probability": pr,
        "Excpected Count": ec,    "Actual": ac, }
display("Initial Calculation", data)
print("Highest Fitness", max(fx))
print()
temp = [i[1]
        for i in sorted([(x, i) for (i, x) in enumerate(ac)], reverse=True)[:2]]
ml = [pl[temp[0]], pl[temp[1]]]
for i in range(5):
    print("-"*70)
    pl = ml
    cl = crossover(pl[0], pl[1])
    ml = mutation(pl[0], pl[1])
    xv = [int(i, 2) for i in ml]
    fx = [customFun(i) for i in xv]
    bestAvg = max(bestAvg, (sum(fx)/len(fx)))


    pr = [i/sum(fx) for i in fx]
    ec = [i/(sum(fx)/len(fx)) for i in fx]
    ac = [round(i) for i in ec]
    data = {"parent": pl,  "crossover": cl,
            "mutation": ml,     "xvalue": xv,        "f(x)": fx}
    display("Generation {}".format(i+1), data)
    data = {"x": xv,    "f(x)": fx,    "parent": pl,    "probability": pr,
        "Excpected Count": ec,    "Actual": ac, }
    display("", data,False)
    print("Highest Fitness", max(fx))
    print()
print("Best Average", bestAvg)
