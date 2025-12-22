# This Module contains functions to anglicize numbers and amounts

# This function anglicizes an integer number between 0 and 999,999
def anglicize(n: int) -> str:
    # Check for non-integer input
    if not isinstance(n, int):
        raise ValueError(f"Invalid input: {n} is not an integer")
    # Check for out of range input
    if n < 0 or n >= 1000000:
        raise ValueError(f"{n} is out of range")

    # Anglicized formats of numbers between 0 and 19
    ones =[
        "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen"
        ]
    # Anglicized formats of tens from 20 to 90
    tens = [
        "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
    # Anglicises numbers between 0 and 19
    if (n < 20):
        return ones[n]
    # Anglicises numbers between 20 and 99
    elif (n >= 20 and n < 100):
        return tens[n // 10 - 2] + ('' if n % 10 == 0 else ' ' + anglicize(n % 10))
    # Anglicises numbers between 100 and 999
    elif (n < 1000):
        return ones[n // 100] + ' Hundred' + ('' if n % 100 == 0 else ' ' + anglicize(n % 100))
    # Anglicises numbers between 1000 and 999,999
    else:
        return anglicize(n // 1000) + ' Thousand' + ('' if n % 1000 == 0 else ' ' + anglicize(n % 1000))

# This function anglicizes a float amount between $0.00 and $999,999.99
def anglicize_amount(amount: float) -> str:
    # Check for valid input
    try:
        # Split the amount into dollars and cents
        dollars, cents = str(f"{amount:.2f}").split('.')
    except ValueError:
        raise ValueError(f"Invalid input: {amount}")
    
    # Convert dollars and cents to integers
    dollars = int(dollars)
    cents = int(cents)
    
    # Check for out of range input
    if amount < 0 or amount >= 1000000:
        raise ValueError(f"{amount} is out of range")
    # Handle zero amount
    elif (amount == 0):
        return f"{anglicize(dollars)} Dollars"
    # Handle amounts with only cents
    elif (dollars == 0):
        return f"{anglicize(cents) + ' Cents'}"
    # Handle amounts with dollars and cents
    else:
        return f"{anglicize(dollars) + ' Dollars'} {'' if (cents == 0) else 'And ' + anglicize(cents) + ' Cents'}"
