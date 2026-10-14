import json
import os
if os.path.exists("expenceTraker.json"):
    if os.path.getsize("expenceTraker.json")==0:
        expenses=[]
        sheet=[]
        cat={}
        total=0
        balance=0
        encome=[]
        earning=0
    else:
        with open("expenceTraker.json","r") as file:
            data=json.load(file)
            expenses=data["expenses"]
            sheet=data["sheet"]
            cat=data["cat"]
            total=data["total"]
            balance=data["balance"]
            encome=data["encome"]
            earning=data["earning"]
else:
    expenses=[]
    sheet=[]
    cat={}
    total=0
    balance=0
    encome=[]
    earning=0
while True:
    print("what do you want to do:")
    print("1.add expense.")
    print("2.want total expense.")
    print("3.want a perticular category expense.")
    print("4.want total income.")
    print("5.add money.")
    print("6.check transaction history.")
    print("7.check balance.")
    print("Stop.")
    a=input("-")
    if a=="1":
        name = input("Enter expense name: ")
        try:
            amount = float(input("Enter expense amount: "))
        except ValueError:
            print("Enter a valid amount")
            continue
        category = input("Enter expense category: ").lower()
        if amount<=0:
            print("invalid")
        elif amount>balance:
            print("insufficient balance.")
        else:    
            total+=amount
            balance-=amount
            expenses.append({"name":name,"amount":amount,"category":category})
            sheet.append({"debit":amount})
            if category in cat:
                cat[category]+=amount
            else:
                cat[category]=amount
    elif a=="2":
        for i in range(0,len(expenses)):
            print(f"{i+1}. {expenses[i]["name"]} | {expenses[i]["amount"]} | {expenses[i]["category"]}")
        print("total: ₹",total)
    elif a=="3":
        try :
            c=input("which category: ").lower()
            q=1
            if cat[c]==0:
                print("no expense.")
            for i in expenses :
                if i["category"]==c:
                    print(f"{q}. {i["name"]} | {i["amount"]} | {i["category"]}")
                    q+=1
            print("total: ₹",cat[c])
        except KeyError:
            print("no expense.")
    elif a=="4":
        for i in range(0,len(encome)):
                    print(f"{i+1}.",encome[i])
        print("your total income: ₹",earning) 
    elif a=="5":
        try:
            money=float(input("Enter the amount: "))
            if money>0:
                balance+=money
                earning+=money
                encome.append(money)
                sheet.append({"credit":money})
            else:
                print("invalid.")
        except ValueError:
            print("choose a valid number")
    elif a=="6":
        for i,a in enumerate(sheet,start=1):
            for key,value in a.items():
                print(f"{i}.{key}: {value}")  
    elif a=="7":
        print("your balance: ₹",balance)
    else:
        break
data={
    "expenses":expenses,
    "sheet":sheet,
    "cat":cat,
    "total":total,
    "balance":balance,
    "encome":encome,
    "earning":earning
}
with open("expenceTraker.json","w") as file:
    json.dump(data,file)
