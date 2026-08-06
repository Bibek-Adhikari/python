# Ask for number of coffees purchased
coffees_purchased = int(input("Enter number of coffees purchased this month: "))

# Set the Constants For Subscriptions, and Coffees
SUBSCRIPTION_FEE = 45.00
INCLUDED_COFFEES = 20
EXTRA_COFFEE_PRICE = 4.50

# Write for additional coffees and extra cost
if coffees_purchased > INCLUDED_COFFEES:
    additional_coffees = coffees_purchased - INCLUDED_COFFEES
    extra_cost = additional_coffees * EXTRA_COFFEE_PRICE
else:
    additional_coffees = 0
    extra_cost = 0.00

# Calculate Total Due Amount
total_due = SUBSCRIPTION_FEE + extra_cost

# Display formatted receipt
print("--- MONTHLY COFFEE SUBSCRIPTION BILL ---")
print(f"Subscription Fee: ${SUBSCRIPTION_FEE:.2f}")
print(f"Coffees Included: {INCLUDED_COFFEES}")
print(f"Additional Coffees: {additional_coffees} x ${EXTRA_COFFEE_PRICE:.2f} = ${extra_cost:.2f}")
print(f"TOTAL DUE: ${total_due:.2f}")
