import check_writer as chkw

print()
# Test cases for anglicize_amount function
try:
    amt = 0.00
    print(f"Amount: {amt} --> {chkw.anglicize_amount(amt)}\n")
except Exception as e:
    print(f"Amount: {amt} --> Error: {e}\n")

try:
    amt = 0.5
    print(f"Amount: {amt} --> {chkw.anglicize_amount(amt)}\n")
except Exception as e:
    print(f"Amount: {amt} --> Error: {e}\n")

try:
    amt = 11.95
    print(f"Amount: {amt} --> {chkw.anglicize_amount(amt)}\n")
except Exception as e:
    print(f"Amount: {amt} --> Error: {e}\n")

try:
    amt = 45
    print(f"Amount: {amt} --> {chkw.anglicize_amount(amt)}\n")
except Exception as e:
    print(f"Amount: {amt} --> Error: {e}\n")

try:
    amt = 100
    print(f"Amount: {amt} --> {chkw.anglicize_amount(amt)}\n")
except Exception as e:
    print(f"Amount: {amt} --> Error: {e}\n")

try:
    amt = 245.75
    print(f"Amount: {amt} --> {chkw.anglicize_amount(amt)}\n")
except Exception as e:
    print(f"Amount: {amt} --> Error: {e}\n")

try:
    amt = 1500
    print(f"Amount: {amt} --> {chkw.anglicize_amount(amt)}\n")
except Exception as e:
    print(f"Amount: {amt} --> Error: {e}\n")

try:
    amt = 34256.33
    print(f"Amount: {amt} --> {chkw.anglicize_amount(amt)}\n")
except Exception as e:
    print(f"Amount: {amt} --> Error: {e}\n")

try:
    amt = 903400.077
    print(f"Amount: {amt} --> {chkw.anglicize_amount(amt)}\n")
except Exception as e:
    print(f"Amount: {amt} --> Error: {e}\n")

try:
    amt = -5.00
    print(f"Amount: {amt} --> {chkw.anglicize_amount(amt)}\n")
except Exception as e:
    print(f"Amount: {amt} --> Error: {e}\n")

try:
    amt = 1000000
    print(f"Amount: {amt} --> {chkw.anglicize_amount(amt)}\n")
except Exception as e:
    print(f"Amount: {amt} --> Error: {e}\n")

try:
    amt = "One Thousand Dollars"
    print(f"Amount: {amt} --> {chkw.anglicize_amount(amt)}\n")
except Exception as e:
    print(f"Amount: {amt} --> Error: {e}\n")
