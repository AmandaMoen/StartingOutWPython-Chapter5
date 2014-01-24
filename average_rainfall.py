# June 8th, 2010
# CS 110
# Amanda L. Moen
# 5. Average Rainfall
# Write a program that uses nested loops to collect data and
# calculate the average rainfall over a period of years.  The
# program should first ask for the number of years.  The outer
# loop will iterate once for each year.  The inner loop will
# iterate twelve times, once for each month.  Each iteration
# of the inner loop will ask the user for the inches of rainfall
# for that month.  After all iterations, the program should
# display the number of months, the total inches of rainfall,
# and the average rainfall per month for the entire period.

def main():
    # Initialize an accumulator variable.
    average = 0.0
    
    # First, ask the user for the number of years that are to be
    # calculated for the average.
    years = input("Enter the number of years you'd like to " +\
                  "get the average rainfall for: ")

    # Months need to start at 0.0 (accumulator variable)
    months = 0.0

    # Set up range for years.
    for year in range(years):
        for count in ['January', 'February', 'March',\
                      'April', 'May', 'June', 'July',\
                      'August', 'September', 'October',\
                      'November', 'December']:

            # Calculate number of months.
            total_months = 12 * years

            # Ask the user for the number of inches of rainfall

    # Print the total rainfall

    # Print how many months

    # Print the average rainfall per month.
        

# Call the main function.
main()
