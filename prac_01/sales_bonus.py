"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Pseudocode:
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""
SALES_THRESHOLD = 1000
SALES_BONUS_10 = 0.1
SALES_BONUS_15 = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < SALES_THRESHOLD:
        bonus = sales * SALES_BONUS_10
    else:
        bonus = sales * SALES_BONUS_15
    print(f"Sales bonus : ${bonus:.0f}")
    sales = float(input("Enter sales: $"))