def calc_bal(annualInterestrate,monthlyPaymentrate,A,num_months):
    if (num_months == 0):
        return(A)
    else:
        b_start = calc_bal(annualInterestrate,monthlyPaymentrate,A,(num_months - 1))
    paid = monthlyPaymentrate * b_start
    unpaid_bal = b_start - paid
    Interest = (annualInterestrate * unpaid_bal) / 12
    balance = unpaid_bal + Interest
    print('Month ' + str(num_months) +'; The remaining balance is ' + format(balance,'.2f'))
    return(float(format(balance,'.2f')))

P = float(input('Enter the total loan amount\n'))
I = float(input('Enter the interest percent for the year in decimal(div by 100)\n'))
M = float(input('Enter the minimum monthly payment rate in decimal(div by 100)\n'))
n = int(input('Enter the number of months at end of which remaining amount is to be calculated\n'))
print(calc_bal(I,M,P,n))
