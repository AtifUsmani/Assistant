import json
import time

tasks = [2, 3]


def text(x):
    tasks.append(str(x))
    print(tasks)


def number(x):
    # tasks.append(int(x))
    tasks.append(int(float(x)))
    print(tasks)
    tasks1 = tasks
    time.sleep(10000)
    with open('listfile.txt', 'w') as filehandle:
        json.dump(tasks1, filehandle)


with open('listfile.txt', 'w') as filehandle:
    json.dump(tasks, filehandle)