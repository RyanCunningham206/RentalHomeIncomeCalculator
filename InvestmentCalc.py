

def calc(purchase_interval, heloc_interval, credit_limit, years):
    duration = years * 12
    house_price = 40000
    credit_limit -= house_price
    houses = 1
    net_rent = 400
    heloc = 0
    income = 0

    #monthly calculations
    for months in range(1, duration + 1):
        cashflow = houses * net_rent

        #end of year summary
        if months % 12 == 0:
            print("")
            print("End of year {:.0f}. You own {} houses.".format(int(months /12), houses))
            print("Monthly Cashflow: $" + str(cashflow), "   Credit Limit: {}".format(int(credit_limit)))
            if (houses * net_rent) - 4000 < 0:
                print("Monthly Take Home Income: $0")
            else:
                print("Monthly Take Home Income:  $" + str(int(income)))

        #debt paydown and shifting to take home profit after more than $4000 monthly coming in
        if cashflow <= 4000:
            credit_limit += cashflow
        else:
            income = (cashflow - 4000) * (3/4)
            if income < 0:
                income = 0
            credit_limit += cashflow - income

        #purchasing new homes with heloc
        if months % heloc_interval == 0:
            houses += 1
            heloc += 1

        #purchasing new homes with available credit
        if credit_limit >= house_price and months % purchase_interval == 0:
            houses += 1
            credit_limit -= house_price




calc(2, 6, 250000, 7)
calc(1, 5, 250000, 7)
calc(2, 5, 250000, 7)
calc(2, 4, 300000, 7)
calc(1, 3, 350000, 7)
calc(1, 2, 250000, 7)
