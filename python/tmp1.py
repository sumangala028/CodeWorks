bill = open("data.txt", "r")
itemIdList = []
itemNameList = []
for line in bill:
    lineList = line.split(",")
    #print(lineList)
    itemIdList.append(lineList[0])
    itemNameList.append(lineList[1])
print(itemIdList)
print (itemNameList)

itemId = -1
while(itemId != 0 ) :
    itemId = input("Enter ID : " )
    index = itemIdList.index(itemId)
    print (index)
    print (itemNameList[index])

print("END")
