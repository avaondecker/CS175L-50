#Ava Ondecker
#CS 175-50 LAB
#2/2/22
#stocks program

num_shares = 2000
purchase_price = 40.0
selling_price = 42.75
commission_rate = 0.03

amountPaidForStock = num_shares * purchase_price

purchaseCommission = commission_rate * amountPaidForStock

totalPaid = amountPaidForStock + purchaseCommission

stockSoldFor = num_shares * selling_price

sellingCommission = commission_rate * stockSoldFor

totalReceived = stockSoldFor - sellingCommission

profitOrLoss = totalReceived = totalPaid


print("Amount paid for stock: $", amountPaidForStock)
print("Profit (or loss if negative): $", profitOrLoss)
print("Commission paid on the sale: $", sellingCommission)
print("Amount the stock sold for: $", stockSoldFor)
print("Commission paid on the purchase: $", purchaseCommission)


            
