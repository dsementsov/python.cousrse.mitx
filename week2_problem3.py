import week2_problem2

balance = 999999
annualInterestRate = 0.18

def minimal_payment_bisection ( balance, annual_interest_rate, epsilon = 0.01):
    """
    Calculate minimum payment to zero your credit in 12 month (using bisection method)

    Input: current balance ( float ), annual interest rate [0:1], optional: epsilon (how close should be the guess)
    Output: Constant payment, incremented by 10
    """
    # If there was no interest, 
    # the debt can be paid off by monthly payments of 1/2 of the balance
    lower_bound = balance / 12

    # monthly payment would be 1/12 of the balance, 
    # after having its interest compounded monthly for an entire year.
    higher_bound = week2_problem2.after_year_balance_recoursive(balance, annual_interest_rate, 0) / 12 
    
    # initial balance
    new_balance = balance
    # initial guess
    payment_guess = 0

    # main bisection loop conditions: balance payed, payed by epsilon marigin
    while new_balance > 0 or abs(new_balance) > epsilon:
        # moving lower bound if the guess is too low
        if new_balance > 0:
            lower_bound = payment_guess
        # moving upper bound if the guess is too high
        elif new_balance < 0:
            higher_bound = payment_guess
        #calculating new guess and balance with new guess
        payment_guess = (higher_bound + lower_bound) / 2
        new_balance = week2_problem2.after_year_balance_recoursive(balance, annual_interest_rate, payment_guess)
    # return result rounded by 2 decimals
    return round(payment_guess, 2)
print ("Lowest payment:", minimal_payment_bisection(balance, annualInterestRate))