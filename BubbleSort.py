
def bubbleSort(*args):
    args = list(args)
    b = 0
    for x in range(len(args) - 1 ):
        for y in range(len(args) -1 - x):
            if args[y] > args[y+1]:
                args[y + 1],args[y] = args[y],args[y+1]
    return list(args)

print(bubbleSort(*(1,5,3,2)))