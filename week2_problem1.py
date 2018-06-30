# Test case values
balance = 560
annualInterestRate = 0.25
monthlyPaymentRate = 0.15

# Iterative solution
def after_year_balance (balance, annual_interest_rate, montly_payment_rate):
    """
    Get your balance at the end of a current year given loan amount and interest rates
    Input: balance (float), annual interest rate (%), minimal monthly payment rate (%)
    Output: balance at the end of a year
    This function use iteration for calculation
    """
    monthly_interest_rate = annual_interest_rate / 12.0
    for i in range(0,12):
        # Calculation payment due this month
        this_month_payment = balance * montly_payment_rate
        # New balance using remaining balance + interest (balance * (interest + 100%))
        balance = (balance - this_month_payment) * (1 + monthly_interest_rate)
    # concating string for nicier output
    newBalanceString = "Remaining balance: " + str(round(balance, 2))
    return (newBalanceString)
print (after_year_balance(balance, annualInterestRate, monthlyPaymentRate))

# Recoursive solution
def after_year_balance_recoursive(balance, annual_interest_rate, montly_payment_rate, current_month = 0):
    """
    Get your balance at the end of a current year given loan amount and interest rates
    Input: balance (float), annual interest rate (%), minimal monthly payment rate (%), optional: current month (1-12)
    Output: balance at the end of a year
    This function use iteration for calculation
    """
    if (current_month == 12):
        return "Remaining balance: " + str(round(balance, 2))
    # calculating montly interest rate
    monthly_interest_rate = annual_interest_rate / 12
    # calculating this month payment
    this_month_payment = balance * montly_payment_rate
    # calculating new balance
    balance = (balance - this_month_payment) * (1 + monthly_interest_rate)
    return after_year_balance_recoursive(balance, annual_interest_rate, montly_payment_rate, current_month + 1)
print (after_year_balance_recoursive(balance, annualInterestRate, monthlyPaymentRate))