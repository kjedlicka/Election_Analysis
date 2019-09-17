savings = float(input("How much do you have in your savings? $"))
interest_rate =float(input("What is the yearly fixed interest? "))
message_to_customer = (
    f"You have ${savings:,.2f} in your savings account. "
    f"The interest rate for your savings account is {interest_rate}. "
    f"Your interest for the year is ${savings * interest_rate:.2f}."
)
print(message_to_customer)