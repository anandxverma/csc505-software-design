# This program calculates the total cost of a meal
# Provided the meal price, it calculates the total cost by adding the tip and tax

# This function formats a Bill Line Item
# Examples of Bill Line Item are Tax, Tip, Meal Price, and Total Cost etc
# Sample Output 1: Meal Price          $10.00
# Sample Output 2: Tip                  $2.00
def format_bill_item(label_txt, amount_txt, separator=" ", max_label_len=30):
    # Format the label and amount
    label_len = len(label_txt)
    amount_txt = amount_txt.rjust(max_label_len - label_len - 1)
    return label_txt + separator + amount_txt

# Constants
TIP_RATE = 0.18                           # 18% tip
TAX_RATE = 0.07                           # 7% tax
MAX_LABEL_LEN = 30                        # Maximum length of the item label used for priniting the output
LABEL_BILL_HEAD = "Bill calculations"     # Maximum length of the item label used for priniting the output

# Ask the user to input the meal price
meal_price = float(input("Enter the price of the meal: $"))

# Calculate the tip amount
# Note: tip is calculated on the pre-tax amount
tip = float(meal_price * TIP_RATE)

# Calculate the tax amount
tax = float(meal_price * TAX_RATE)

# Calculate total cost
total_cost = meal_price + tip + tax

# Print the results
print("=" * MAX_LABEL_LEN)
print(LABEL_BILL_HEAD)
print(format_bill_item("Meal price", f"${meal_price:.2f}"))
print("-" * MAX_LABEL_LEN)
print(format_bill_item("Tip @" + f"{TIP_RATE * 100:.2f}" + "%", f"${tip:.2f}"))
print(format_bill_item("Tax @" + f"{TAX_RATE * 100:.2f}" + "%", f"${tax:.2f}"))
print("-" * MAX_LABEL_LEN)
print(format_bill_item("Total cost", f"${total_cost:.2f}"))
print("=" * MAX_LABEL_LEN)