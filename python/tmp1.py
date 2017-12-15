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

bill = open("data.txt", "r").read().split(",")

print ("\tROLEX BAKE MART")
print ("ID\tItem\tPrice\tStock\n")
for li in bill:
    print (li,end='\t')
    lineList = li.split(",")
order = input("\nPLese enter the item ID: ")
print (bill[order-1])

while order != 0:
    qty = input("Please enter item quantity :")
print ("Bill statement")
i = 1
print ("Bill ID", i)
from datetime import datetime
now = datetime.now()
print ("Date : %s-%s-%s  %s:%s\n" %((now.year),(now.month), (now.day),(now.hour), (now.minute)))

print ("Item\tQty\tTot\n")
print ("%s\t%s\t%s" % qty)
i = i + 1
        



