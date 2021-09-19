currency_names_list = [
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

labels = [
"Cash in Five Thousand Rupees",
"Cash in One Thousand Rupees",
"Cash in Five Hundred Rupees",
"Cash in One Hundred Rupees",
"Cash in Fifty Rupees",
"Cash in Twenty Rupees",
"Cash in Ten Rupees",
"Cash in Five Rupees",
"Cash in Two Rupees",
"Cash in One Rupees"
]

remaining_cash = [
["FIVE THOUSAND", 5000000],
["ONE THOUSAND", 1000000], 
["FIVE HUNDRED", 500000], 
["ONE HUNDRED", 1000000], 
["FIFTY", 500000], 
["TWENTY", 20000], 
["TEN", 10000], 
["FIVE", 5000],
["TWO", 2000],
["ONE", 1000]
]

def check_cash_register(price, cash, currency_names_list=remaining_cash):
    status = get_status(price, cash, currency_names_list)
    change = get_change(price, cash, currency_names_list, status)
    return {
        "status": status,
        "change": change
    }


def get_status(price, cash, currency_names_list):
    cash_in_drawer_list = currency_names_list
    cinda = []
    cash_in_drawer = 0
    for item in cash_in_drawer_list:
        cinda.append(item[1])
        cash_in_drawer += item[1]
    ac = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
    status = ""
    total_change = float(cash) - float(price)
    if total_change > cash_in_drawer:
        status = "INSUFFICIENT_FUNDS"
    elif total_change == cash_in_drawer:
        status = "CLOSED"
    else:
        status = "OPEN"
        i = 0
        while i < len(cinda):
            if total_change >= ac[i] and cinda[i] >= ac[i]:
                total_change -= ac[i]
                cinda[i] -= ac[i]
                total_change = float(format(total_change, ".2f"))
                cinda[i] = float(format(cinda[i], ".2f"))
            else: 
                i += 1
      
        if total_change != 0:
            status = "INSUFFICIENT_FUNDS"

    return status


def get_change(price, cash, currency_names_list, status):
    total_change = float(cash) - float(price)
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
    cash_in_drawer_list = currency_names_list
    i = 0
    j = 0
    while i < len(ac):
        if total_change >= ac[i][1] and cash_in_drawer_list[i][1] >= ac[i][1]:
            total_change -= ac[i][1]
            cash_in_drawer_list[i][1] -= ac[i][1]
            total_change = float(format(total_change, ".2f"))
            cash_in_drawer_list[i][1] = float(format(cash_in_drawer_list[i][1], ".2f"))
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