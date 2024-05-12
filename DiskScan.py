from random import randint

# Creates all the Request
def create_request():
    file = open("disk_request.txt", "w")
    for x in range(0, 1000):
        file.write(str(randint(0, 4999)) + "\n")

def fcfs(file, head):
    file = open(file, "r")
    lines = file.readlines()
    for index, line in enumerate(lines):
        lines[index] = int(line.replace("\n", ''))
    # Goes from one request to the other First Come First Serve
    totalHeadMovement = 0
    firstHead = 0
    secondHead = head
    for headmovement in lines:
        firstHead = secondHead
        secondHead = headmovement
        movement = abs(abs(firstHead) - abs(secondHead))
        totalHeadMovement = totalHeadMovement + movement
    return totalHeadMovement

def scan(file, head, direction):
    file = open(file, "r")
    lines = file.readlines()
    for index, line in enumerate(lines):
        lines[index] = int(line.replace("\n", ''))
    # Goes from left to right or right to left in a bounce sequence
    # Rearrange List
    lines.sort()
    # Find the index Number
    indexPoint = 0
    X = False
    while X == False:
        for indexNumber, lineNumber in enumerate(lines):
            if head < lineNumber:
                indexPoint = indexNumber
                X = True
    
    # Count Movement
    totalHeadMovement = 0
    firstHead = 0
    secondHead = head
    for headmovement in lines:
        firstHead = secondHead
        secondHead = headmovement
        movement = abs(abs(firstHead) - abs(secondHead))
        totalHeadMovement = totalHeadMovement + movement
    return totalHeadMovement


filename = str(input("State the File: "))
head = int(input("State the current Head: "))
direction = str(input("Direction the of the Head: "))

print(scan(filename, head, direction))