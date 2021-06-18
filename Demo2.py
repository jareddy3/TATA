def swaplist(newlist):
    size = len(newlist)

    # Swapping
    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1] = temp

    return newlist
# Driver code
newlist = [12, 35, 9, 56, 24]

print(swapList(newlist))