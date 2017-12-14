bill = open("data.txt" , "r")
print ("\tROLEX BAKE MART")
print ("ID\tItem\tPrice\tStock")

    
itemIdList = []
itemNameList = []
itemPriceList = []
for line in bill:
    lineList = line.split(",")
    itemIdList.append(lineList[0])
    itemNameList.append(lineList[1])
    itemPriceList.append(lineList[2])
print (itemIdList)
print (itemNameList)
print (itemPriceList)

i = 1
itemId = -1
while (itemId != 0):
    itemId = input("Please Input Item ID :")
    if (itemId in itemIdList):
        index = itemIdList.index(itemId)
        print (itemId,end='\t')
        print (itemNameList[index],end='\t')
        print ("RS.",itemPriceList[index])
        qty = input("Please Input the quantity")
    else :
        print ("Bill Statement")
        print ("Bill ID :", i)
        from datetime import datetime
        now = datetime.now()
        print ("Date : %s-%s-%s  %s:%s\n" %((now.year),(now.month), (now.day),(now.hour), (now.minute)))
        print ("\nItem\tQTY\tTot")
        print ("%s\t%s\t%s" % itemId, qty,itemPriceList[index]*qty)
        i = i + 1
    
