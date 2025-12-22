************************************************
MODULE: check_writer.py
************************************************

The check_writer.py is a Python Module containing functions to anglicize numbers and Dollar amounts. The module works with numbers from 0 to 999,999 for the amount and number values. The Module has two functions as described below:

************************************************
FUNCTION: Anglicize an Integer
************************************************
This function converts any integer between 0 and 999,999 into English words. For example, the number "352" will be presented as "Three hundred fifty-two."

The function is based on the premise that we need to establish logic for converting unique values first, specifically the numbers from 0 to 19 (Zero, One, Two, etc.) and the tens multiples from 20 to 90 (Twenty, Thirty, Forty, etc.).

The remaining numbers are formed by combining one or more of these unique formats with "Hundred" and/or "Thousand." For instance, the number 23 is represented as "Twenty Three," 119 becomes "One Hundred Nineteen," and 1145 is expressed as "One Thousand One Hundred Forty Five."

SPECIFICATIONS
------------------------------------------------
SIGNATURE: anglicize(n: int) -> str
INPUT: An integer between 0 and 999,999
OUTPUT: Anglicised format of the input number
EXCEPTIONS:
- Number Out of Range for numbers outside the 0 to 999,999
- Invalid Input Value for invalid values, such as strings or alphanumeric values
ASSUMPTIONS:
- The input value is an integer between 0 to 999,999.

************************************************
FUNCTION: Anglicize Amount
************************************************
This function converts any dollar amount between 0 and 999,999 into English words. For example, the amount "260.75" will be expressed as "Two hundred sixty dollars and seventy-five cents."

First, the input value is split into a Dollar and a Cent component. Next, both the Dollar and Cent values are converted to their English-language equivalents using the "Anglicize Integer" function described previously. Finally, the anglicized formats of the Dollar and Cent values are combined, with the words "Dollar" and "Cents" appended for the final output. The function also validates the inputs and handles cases where the amount is a whole number (i.e., 0 Cents) or a sub-dollar value (i.e., less than 1 Dollar).

SPECIFICATIONS
------------------------------------------------
SIGNATURE: anglicize_amount(n: float) -> str
INPUT: A float between 0 and 999,999
OUTPUT: Anglicised format of the input amount
EXCEPTIONS:
- Amount Out of Range for values outside the 0 to 999,999
- Invalid Input Value for invalid values, such as strings or alphanumeric values
ASSUMPTIONS:
- The input value is any numeric value between 0 to 999,999.