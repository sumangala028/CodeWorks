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


itemId = -1
while (True):
    itemId = input("Please Input Item ID :")
    if (itemId in itemIdList):
        index = itemIdList.index(itemId)
        indexList.append(index)
        print (itemId,end='\t')
        print (itemNameList[index],end='\t')
        print ("RS.",itemPriceList[index])
        qty = input("Please Input the quantity\n")
        qtyList.append(qty)

    else :
        break
i = 0
print ("Bill Statement")
print ("Bill ID :%s" % (i+1))
from datetime import datetime
now = datetime.now()
print ("Date : %s-%s-%s  %s:%s" %((now.year),(now.month), (now.day),(now.hour), (now.minute)))
print ("\nItem\tPrice\tQTY\tTot")

totalBill = 0
total = 0
for indx in indexList:
    print (itemNameList[indx],end="\t")
    print (itemPriceList[indx],end="\t")
    print (qtyList[i], end="\t")
    total = int(itemPriceList[i]) * int(qtyList[i])
    print (total)
    totalBill = totalBill + total
    i = i + 1


print ("===========================")
print ("subTotal :",end="\t\t") 
print (totalBill)


    
