from random import choice
import re

test = dict()

with open("Generators/book.txt", "r") as book:
    start = [str(i) for i in re.split(r'[.!?-]',book.read())]

print(f"Count of sentenses: {len(start)}")

for i in range(len(start)):
    new = [str(i) for i in start[i].split()]
    new.insert(0, "*START*")
    new.append("*END*")

    for i in range(len(new)-1):
        if new[i] not in test:
            test[new[i]] = {new[i+1]: 1}
        else:
            if new[i+1] not in test[new[i]]:
                test[new[i]][new[i+1]] = 1
            else:
                test[new[i]][new[i+1]] += 1

print("Done")

while True:
    if input() == "w":
        temp = choice(list(test['*START*'].keys()))
        a = [temp]
        while temp != "*END*":
            b = choice(list(test[temp].keys()))
            if b == "*END*":
                break
            temp = b
            a.append(temp)

        #printing all a, if len(a) < 20
        answer = " ".join(a[i] for i in range(min(len(a)-1,20))) + "."
        print(f'{answer.capitalize()}')

