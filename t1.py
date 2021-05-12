#for x in range(6, 0, -1):
    #for y in range(x):
    #for
    #    print("*", end=" ")
    #print(" ")



k = -1
for i in range(6, 0, -1):

    for j in range(k+1, 0, -1):
        print(end=" ")
    k = k + 2

    for j in range(i):
        print("* ", end="")

    print("")


