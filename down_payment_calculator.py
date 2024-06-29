def calc_savings_needed():
    """
    Calculates the best savings rate needed to afford a down payment on a dream home within three years.
    If it's determined that saving the down payment within 3 years is impossible, the function prints a
    corresponding message. Otherwise, it prints the best savings rate found and the number of steps taken
    in the bisection search.
    """
    annual_salary_real = float(input("Enter the starting salary: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi annual raise as decimal: "))
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    monthly_salary = annual_salary_real / 12

    # Set up a bisection search. The purpose of this code is to efficiently find the optimal savings rate
    # that allows the user to save enough money for a down payment on a house within three years.
    # The bisection search method is used because it is an efficient way to zero in on the correct
    # savings rate by repeatedly narrowing down the range of possible rates.
    months = 36
    epsilon = 100
    low = 0.0
    high = 1.0
    guess = (low + high) / 2.0
    num_guesses = 0
    breaked = False

    while abs(current_savings - total_cost * portion_down_payment) > epsilon:
        if guess == 1.0:
            breaked = True
            break
        # print("new guess: ",guess)
        annual_salary = annual_salary_real
        monthly_salary = annual_salary / 12
        num_guesses += 1

        month = 0
        current_savings = 0
        while month < months:
            current_savings += (current_savings * r / 12) + (guess * monthly_salary)
            month += 1
            if (month % 6) == 0:
                annual_salary += annual_salary * semi_annual_raise
                monthly_salary = annual_salary / 12

        if abs(current_savings - (total_cost * portion_down_payment)) > epsilon:
            # print("current_savings: ",current_savings)
            if current_savings < (total_cost * portion_down_payment):
                low = guess
            else:
                high = guess
            guess = (low + high) / 2.0

    if breaked:
        print("It is not possible to pay down payment in 3 years.")
    else:
        print("Best savings rate: ", guess)
        print("Number of months: ", num_guesses)


calc_savings_needed()
