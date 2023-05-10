#Initialising variables
capacity1 = int(input())
capacity2 = int(input())
target = int(input())
jug1, jug2 = 0, 0
states = [jug1, jug2]

#Logic
if(capacity1 < target or capacity2 < target):
        print("solution is not possible")
else:
    for i in range(1):
        while jug1 != target and jug2 != target:
            states = [jug1, jug2]
            print (states)
            if jug2 < capacity2:
                if jug1 != 0:
                    if jug2+jug1 <= capacity2:
                        jug2 += jug1
                        jug1 = 0
                        print("Transfer")
                    else:
                        n = jug1+jug2-capacity2
                        jug2 = capacity2
                        jug1 = n
                        print("Transfer")
                else:
                    jug1 = capacity1
                    print("Fillr")
            else:
                jug2 = 0
                print("Empty")
            
        print([jug1, jug2], "Solution Found")