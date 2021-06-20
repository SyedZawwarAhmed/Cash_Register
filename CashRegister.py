def checkCashRegister(price, cash, cid):
    status = getStatus(price, cash, cid)
    change = getChange(price, cash, cid, status)
    return {
        "status": status,
        "change": change
    }


def getStatus(price, cash, cid):
    cashInDrawerArray = cid
    cinda = []
    cashInDrawer = 0
    for item in cashInDrawerArray:
        cinda.append(item[1])
        cashInDrawer += item[1]
    ac = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
    status = ""
    totalChange = cash - price
    if totalChange > cashInDrawer:
        status = "INSUFFICIENT_FUNDS"
    elif totalChange == cashInDrawer:
        status = "CLOSED"
    else:
        status = "OPEN"
        i = 0
        while i < len(cinda):
            if totalChange >= ac[i] and cinda[i] >= ac[i]:
                totalChange -= ac[i]
                cinda[i] -= ac[i]
                totalChange = float(format(totalChange, ".2f"))
                cinda[i] = float(format(cinda[i], ".2f"))
            else: 
                i += 1
      
        if totalChange != 0:
            status = "INSUFFICIENT_FUNDS"

    return status


def getChange(price, cash, cid, status):
    totalChange = cash - price
    changeArray = []
    currentCurrencyName = ""
    currentCurrency = 0
    change = []
    ac = [
    ["FIVE THOUSAND", 5000],
    ["ONE THOUSAND", 1000],
    ["FIVE HUNDRED", 500],
    ["ONE HUNDRED", 100],
    ["FIFTY", 50],
    ["TWENTY", 20],
    ["TEN", 10],
    ["FIVE", 5],
    ["TWO", 2],
    ["ONE", 1]
    ]
    cashInDrawerArray = cid
    i = 0
    j = 0
    while i < len(ac):
        if totalChange >= ac[i][1] and cashInDrawerArray[i][1] >= ac[i][1]:
            totalChange -= ac[i][1]
            cashInDrawerArray[i][1] -= ac[i][1]
            totalChange = float(format(totalChange, ".2f"))
            cashInDrawerArray[i][1] = float(format(cashInDrawerArray[i][1], ".2f"))
            j += 1
        else:
            if j != 0:
                currentCurrencyName = ac[i][0]
                currentCurrency = ac[i][1] * j
                if status != "INSUFFICIENT_FUNDS":
                    change = [currentCurrencyName, currentCurrency]
                    changeArray.append(change)
            j = 0
            i += 1
    return changeArray

cid = [
["FIVE THOUSAND"],
["ONE THOUSAND"],
["FIVE HUNDRED"],
["ONE HUNDRED"],
["FIFTY"],
["TWENTY"],
["TEN"],
["FIVE"],
["TWO"],
["ONE"]
]
print("Enter Cash in Drawer")
for item in cid:
    x = int(input("Cash in " + item[0] + " Rupee/s:- "))
    item.append(x)

price = int(input("Enter Amount Due:- "))
cash = int(input("Enter Cash Given:- "))
    
print(checkCashRegister(price, cash, cid))

# 1000, 2000, [["ONE", 24], ["TWO", 52], ["FIVE", 625], ["TEN", 540], ["TWENTY", 2640], ["FIFTY", 23450], ["ONE HUNDRED", 456300], ["FIVE HUNDRED", 32432500], ["ONE THOUSAND", 354234000], ["FIVE THOUSAND", 23565000]]