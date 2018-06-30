balance = 4773
annualInterestRate = 0.2

# Using AR(1) model decomposition
def minimal_payment_ar (balance, annual_interest_rate):
    """
    This function will calculate necessary amount of month to month payment to pay up the loan in 12 month
    
    Input: credit balance (int/float, positive), annual interest rate (float, %)
    Output: required amount to pay each month rounded up to 10
    """
    # Use AR(1) model decomposition where 
    # y12 = p = (y11 - p) * (1 + MR) | p + p(1+MR) = y11(1+MR) == p(1+(1+MR)) = y11(1+MR)
    # where y is balance to this month 
    # MR is monthly interest rate
    # p is necessary payment per month to zero out your balance
    # therefore as y11 = (y10 - payment) * (1 + MR) we substitute for y in [y11:y0]
    # rearanging p = y0 (1+MR)^12 / (1+MR)^0 + (1+MR)^1 + (1+MR)^2 +...+ (1+MR)^11
    #  where y0 is initial balance
    #  using geometrical progression with r = 1+MR, n = 12 collapse denominator into (1+MR)^12 - 1 / MR
    # rearange the formula before calculating : p = y0 * (1+MR)^12 * MR / (1+MR)*12 - 1
    
    # getting monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12
    
    # calculating denominator
    denominator = (1+monthly_interest_rate)**12 - 1
    
    # calculating nominator
    nominator = balance * ( 1 + monthly_interest_rate )**12 * monthly_interest_rate
    
    payment = nominator / denominator
    
    # returning payment. Always round up to nearest 10
    return (round(int(payment)+5, -1))
    
print ("Lowest payment: " + str(minimal_payment_ar(balance, annualInterestRate)))

# using recursion

# helper method for balance after 12 month
def after_year_balance_recoursive(balance, annual_interest_rate, monthly_payment, current_month = 0):
    """
    Get your balance at the end of a current year

    Input: balance (float), annual interest rate (%) [0:1], monthly payment in $, optional: current month (1-12)
    Output: balance at the end of a year
    This function use iteration for calculation
    """
    if (current_month == 12):
        return balance
    
    monthly_interest_rate = annual_interest_rate / 12
    
    balance = (balance - monthly_payment) * (1 + monthly_interest_rate)
    
    return after_year_balance_recoursive(balance, annual_interest_rate, monthly_payment, current_month + 1)

# method for finding minimal payment
def minimal_payment_rec(balance, annual_interest_rate, payment_guess = 10):
    """
    Calculate minimum payment to zero your credit in 12 month

    Input: current balance ( float ), annual interest rate [0:1]
    Output: Constant payment, incremented by 10
    """
    
    # Use helper function to calculate new balance in 12 month
    new_balance = after_year_balance_recoursive(balance, annual_interest_rate, payment_guess)
    
    # We found our guess if new balance in smaller that 0, return paymen guess
    if new_balance <= 0:
        return "Lowest payment: " + str(payment_guess)
    
    # Recurse with incrementing payment guess if we dont
    return minimal_payment_rec(balance, annual_interest_rate, payment_guess + 10)

print (minimal_payment_rec(balance, annualInterestRate))




