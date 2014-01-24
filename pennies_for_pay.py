# June 8th, 2010
# CS 110
# Amanda L. Moen
# 7. Pennies for Pay
# Write a program that calculates the amount of money a person
# would earn over a period of time if his or her salary is one
# penny the first day, two pennies the second day, and continues
# to double each day.  The program should ask the user for the
# number of days.  Display a table showing what the salary was
# for each day, and then show the total pay at the end of the
# period.  The output should be displayed in a dollar amount,
# not the number of pennies.

def main():
    
    # Ask the user how many days they worked.
    ndays = input('Enter the number of days worked: ')
    pay = 0.005 # my starting salary
    
    # Create the function to calculate the pay per day.
    for day in range(1,ndays+1):
        #pay = pay * 2.0
        pay *= 2.0
        print ' Day', day, ' Salary', pay

    # State the results of the function.
    print 'Your salary on day', ndays, 'would be $%.2f' % pay

# Call the main function.
main()

