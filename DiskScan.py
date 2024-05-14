from random import randint
import copy

# Creates all the Request
def create_request():
    file = open("disk_request.txt", "w")
    for x in range(0, 1000):
        file.write(str(randint(0, 4999)) + "\n")

def fcfs(initial, head):
    lines = copy.deepcopy(initial)
    totalHeadMovement = 0
    firstHead = 0
    secondHead = head
    for headmovement in lines:
        firstHead = secondHead
        secondHead = headmovement
        movement = abs(abs(firstHead) - abs(secondHead))
        totalHeadMovement = totalHeadMovement + movement
    return totalHeadMovement

def scan(initial, head):
    lines = copy.deepcopy(initial)
    FinishedRequest = []
    currentHead = head
    direction = True
    while len(lines) >= 1:
        RemovedRequest = []
        for index, request in enumerate(lines):
            if request <= currentHead and direction == False:
                currentHead = request
                FinishedRequest.append(request)
                RemovedRequest.append(request)
            elif request >= currentHead and direction == True:
                currentHead = request
                FinishedRequest.append(request)
                RemovedRequest.append(request)
        for remove in RemovedRequest:
            lines.remove(remove)
        if direction == False and len(lines) >= 1:
            FinishedRequest.append(0)
            direction = True
        elif direction == True and len(lines) >= 1:
            FinishedRequest.append(5000)
            direction = False
    totalHeadMovement = 0
    firstHead = 0
    secondHead = head
    for headmovement in FinishedRequest:
        firstHead = secondHead
        secondHead = headmovement
        movement = abs(abs(firstHead) - abs(secondHead))
        totalHeadMovement = totalHeadMovement + movement
    return totalHeadMovement

def CScan(initial, head):
    lines = copy.deepcopy(initial)
    FinishedRequest = []
    currentHead = head
    direction = True
    while len(lines) >= 1:
        RemovedRequest = []
        for index, request in enumerate(lines):
            if request >= currentHead and direction == True:
                currentHead = request
                FinishedRequest.append(request)
                RemovedRequest.append(request)
        for remove in RemovedRequest:
            lines.remove(remove)
        if len(lines) >= 1:
            FinishedRequest.append(0)
            currentHead = 0

    totalHeadMovement = 0
    firstHead = 0
    secondHead = head
    for headmovement in FinishedRequest:
        firstHead = secondHead
        secondHead = headmovement
        movement = abs(abs(firstHead) - abs(secondHead))
        totalHeadMovement = totalHeadMovement + movement
    return totalHeadMovement

filename = str(input("State the File: "))
head = int(input("State the current Head: "))
file = open(filename, "r")
lines = file.readlines()
for index, line in enumerate(lines):
        lines[index] = int(line.replace("\n", ''))
linesSorted = copy.deepcopy(lines)
linesSorted.sort()

print(f'''
# Table of Results :
# Non-Sorted
# FCFS   : {fcfs(lines, head)}
# Scan   : {scan(lines, head)}
# C-Scan : {CScan(lines, head)}

# Sorted
# FCFS   : {fcfs(linesSorted, head)}
# Scan   : {scan(linesSorted, head)}
# C-Scan : {CScan(linesSorted, head)}
# ''')