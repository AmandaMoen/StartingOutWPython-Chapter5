# June 8th, 2010
# CS 110
# Amanda L. Moen
# 3. Budget Analysis
# Write a program that asks the user to enter the amount that
# he or she has budgeted for a month.  A loop should then
# prompt the user to enter each of his or her expenses for
# the month, and keep a running total.  When the loop
# finishes, the program should display the amount that the user
# is over or under budget.

def main():
    # Ask the user for their budget for the month.
    budget = input('What is your budget for the month? ')

    # Create a variable to control the loop.
    keep_going = 'y'

    # Calculate a series of expenses.
    while keep_going == 'y':
        # Ask the user to enter an expense.
        expense = input('Enter an expense: ')

        # Calculate the remainder of the budget.
        budget = budget - expense

        # State what the remaining budget is.
        print 'Your remaining budget is $%.2f.' % budget

        # Ask the user if they'd like to enter another expense.
        keep_going = raw_input('Do you want to calculate another ' +\
                               'expense (Enter y for yes): ')
        
# Call the main function.
main()
