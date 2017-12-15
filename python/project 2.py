bill = open("data.txt" , "r")
print ("\tROLEX BAKE MART")
print ("ID\tItem\tPrice\tStock")

    
itemIdList = []
itemNameList = []
itemPriceList = []
indexList = []
qtyList = []
total = 0
for line in bill:
    lineList = line.split(",")
    itemIdList.append(lineList[0])
    itemNameList.append(lineList[1])
    itemPriceList.append(lineList[2])
print (itemIdList)
print (itemNameList)
print (itemPriceList)

i = 0
itemId = -1
while (True):
    itemId = input("Please Input Item ID :")
    if (itemId in itemIdList):
        index = itemIdList.index(itemId)
        indexList.append(index)
        print (itemId,end='\t')
        print (itemNameList[index],end='\t')
        print ("RS.",itemPriceList[index])
        qty = input("Please Input the quantity")
        qtyList.append(qty)

    else :
        break
    
def computeBill(order):
    total = 0
    for item in order:
        total = itemPriceList[item] * qtyList[item]
        return total
    
    print ("Bill Statement")
    print ("Bill ID :%s" % (i+1))
    from datetime import datetime
    now = datetime.now()
    print ("Date : %s-%s-%s  %s:%s\n" %((now.year),(now.month), (now.day),(now.hour), (now.minute)))
    print ("\nItem\tQTY\tTot")
    print ("%s\t%s\t%s" % itemIdList[item], qtyList[item], total)
    i = i + 1
    computeBill(index)

    
