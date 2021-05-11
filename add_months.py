"""A function to add months to a datetime object"""

from datetime import datetime

def days_in_month(month, year):
    """
    Returns the number of days
    in given month
    """
    # Months that have 31 days
    long_months = [1, 3, 5, 7, 8, 10, 12]

    # Now move date forward
    if month == 2:
        if year % 4 == 0:
            return 29
        else:
            return 28
    elif month in long_months:
        return 31
    else:
        return 30

def get_new_month(date, num_of_months):
    """
    Adds month to date, if current is December
    returns a tuple with new month and new year
    otherwise returns tuple with new_month and None
    """
    if num_of_months <= 12:
        new_month = date.month + num_of_months

        if new_month > 12 and new_month < 24:
            new_month -= 12
            new_year = date.year +1
            return (new_month, new_year)
        elif new_month < 12:
            return (new_month, None)


def add_months(date, num_of_months):
    """Moves date forward by given number of months"""
    new_details = get_new_month(date, num_of_months)
    print(new_details)

    if new_details[1] != None:
        days_in_new_month = days_in_month(new_details[0], new_details[1])
    else:
        days_in_new_month = days_in_month(new_details[0], date.year)

    if date.day > days_in_new_month:
        day = days_in_new_month
    else:
        day = date.day
    
    if new_details[1] != None:
        return datetime(new_details[1], new_details[0], day)
    else:
        return datetime(date.year, new_details[0], day)
