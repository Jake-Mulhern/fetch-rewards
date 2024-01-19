import math
import decimal

def alphanumeric_count(string):
    """
    Counts each alphanumeric character in a string.
    """
    total = 0;
    for char in string:
        if char.isalnum():
            total += 1
    
    return total

def is_integer(total):
    """
    Checks a number and determines if it is an integer.
    """
    if total % 1 == 0:
        return True
    return False
    
def is_quarter_factor(total):
    """
    If the total is evenly divided by .25 returns True.
    """
    if total % decimal.Decimal('.25') == 0:
        return True
    return False

def is_third_factor(string):
    """
    If length of string is evenly divided by 3 returns True.
    """
    if len(string) % 3 == 0:
        return True
    return False

def is_odd(num):
    """
    If number is odd returns True.
    """
    if num % 2 != 0:
        return True
    return False

def is_in_time_range(start, end, time):
    """
    If the specified time is with the specified time range returns True.
    """
    if start <= time < end:
        return True
    return False

def sum_points(receipt, items):
    """
    Calculates the number of points gained from a given Receipt.
    """
    total_points = 0

    ## 1 point for each alphanumeric character in retailer name
    total_points += alphanumeric_count(receipt.retailer)

    ## 50 pts if total is a round dollar amount with no cents
    if is_integer(receipt.total):
        total_points += 50

    ## 25 points if the total is a multiple of 0.25
    if is_quarter_factor(receipt.total):
        total_points += 25
  
    ## 5 pts for every two items on the receipt
    total_points += math.floor(items.count() / 2) * 5
  
    ## If the trimmed length of the item description is a multiple of 3,
    for item in items:
        if is_third_factor(item.shortDescription.strip()):
            ## multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
            total_points += math.ceil(item.price * decimal.Decimal(.2))

    ## 6 pts if the day in the purchase date is odd
    if is_odd(receipt.purchaseDate.day):
        total_points += 6

    ## 10 pts if time of purchase is after 2pm and before  4pm
    if is_in_time_range(14, 16, receipt.purchaseTime.hour):
        total_points += 10

    return total_points
  