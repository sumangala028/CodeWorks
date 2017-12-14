bill = open("data.txt", "r").read().split(",")

print ("\tROLEX BAKE MART")
print ("ID\tItem\tPrice\tStock\n")
for li in bill:
    print (li,end='\t')
    
order = input("\nPLese enter the item ID: ")
print (li[0])

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
        



    
    
