import sys

class tax_level:
    income = 0
    rate = 0.0
    deduct = 0
    def __init__(self, income_, rate_, deduct_):
        self.income = income_
        self.rate = rate_
        self.deduct = deduct_

tax_level_list = []

def make_all_tax_level():
    tax_level_1 = tax_level(36000, 0.03, 0)
    tax_level_2 = tax_level(144000, 0.10, 2520)
    tax_level_3 = tax_level(300000, 0.20, 16920)
    tax_level_4 = tax_level(420000, 0.25, 31920)
    tax_level_5 = tax_level(660000, 0.30, 52920)
    tax_level_6 = tax_level(960000, 0.35, 85920)
    tax_level_7 = tax_level(1000000000, 0.45, 181920)
    tax_level_list.append(tax_level_1)
    tax_level_list.append(tax_level_2)
    tax_level_list.append(tax_level_3)
    tax_level_list.append(tax_level_4)
    tax_level_list.append(tax_level_5)
    tax_level_list.append(tax_level_6)
    tax_level_list.append(tax_level_7)

def get_tax_level(income):
    for tl in tax_level_list:
        if income < tl.income:
            #print "get_tax_level:", tl.income, tl.rate
            return tl

def run(argvs):
    if len(argvs) != 3:
        print "input argv num wrong"
        return
    #month_income = 50000
    #month_deduct = 5000 + 4500
    month_income = int(argvs[1])
    month_deduct = int(argvs[2])
    if month_income < month_deduct:
        print "input wrong: month_income:", month_income, " less than month_deduct:", month_deduct
        return

    make_all_tax_level()
    print "month_income:", month_income, " month_deduct:", month_deduct

    all_income = 0
    all_tax_income = 0
    all_tax = 0.0

    for i in range(1,13):
        all_income += month_income
        all_tax_income += month_income - month_deduct
        tl = get_tax_level(all_tax_income)
        tax = all_tax_income * tl.rate - tl.deduct - all_tax
        all_tax += tax
        print "month:", i ," all_income:", all_income, " tax_rate:", tl.rate, " month_tax:", tax, " all_tax:", all_tax 

if __name__ == "__main__":
    run(sys.argv)

