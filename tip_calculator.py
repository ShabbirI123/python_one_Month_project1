#Tip calculator!
# User has to give the bill amount and the program will give three 
# options to select a standard tip. After choosing a tip, it will 
# compute the total amount.

bill = input("How much is the bill: ")

bill_amount = bill.replace("$", "")

print("How much tip do yu want to give? \n 1) 15% tip \n 2) 18% tip \n 3) 20% tip")

choice = input("Please selcet a the desired tip by typing a number from 1 to 3")

if choice == "1":
	print(f"Total amount: {(float(bill_amount)*0.15)+float(bill_amount)} $")

if choice == "2":
	print(f"Total amount: {(float(bill_amount)*0.18)+float(bill_amount)} $")

if choice == "3":
	print(f"Total amount: {(float(bill_amount)*0.20)+float(bill_amount)} $")