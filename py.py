"""
Skill Builders: Riverside Kayak Rentals
------------------------------------------------
COMPLETED. All 4 functions implemented.

Unlike a full checkout program, these are 4 SEPARATE, self-contained
challenges. Each one exercises a skill you'll need for Assessment 2,
but none of them ask you to build one continuous input-driven program.
Run this file directly (no typing needed) and check the printed output
against the expected results noted in the practice activity doc.
"""

# Equipment catalogue - a dictionary of dictionaries (given, not something
# you need to build from scratch this time).
equipment = {
    "Single Kayak":          {"rate_per_hour": 15.00, "type": "watercraft"},
    "Double Kayak":          {"rate_per_hour": 25.00, "type": "watercraft"},
    "Stand-Up Paddleboard":  {"rate_per_hour": 12.00, "type": "watercraft"},
    "Life Jacket":           {"rate_per_hour": 3.00,  "type": "safety gear"},
    "Dry Bag":               {"rate_per_hour": 2.00,  "type": "accessory"},
    "Waterproof Phone Case": {"rate_per_hour": 1.50,  "type": "accessory"},
}


# ===========================================================
# Challenge 1: Look Up & Filter
# ===========================================================
def get_rate(equipment, item_name):
    """
    Return the hourly rate for item_name, or None if it isn't in the
    catalogue.
    """
    if item_name in equipment:
        return equipment[item_name]["rate_per_hour"]
    return None


def list_by_type(equipment, type_name):
    """
    Return a list of item names whose "type" matches type_name.
    e.g. list_by_type(equipment, "accessory") -> ["Dry Bag", "Waterproof Phone Case"]
    (order doesn't matter)
    """
    return [name for name, details in equipment.items() if details["type"] == type_name]


def most_expensive_item(equipment):
    """
    Return a tuple (name, rate) for the item with the highest rate_per_hour.
    """
    name = max(equipment, key=lambda item_name: equipment[item_name]["rate_per_hour"])
    return name, equipment[name]["rate_per_hour"]


# ===========================================================
# Challenge 2: Process a Booking Log
# ===========================================================
# A booking is given as a list of (item_name, hours) tuples - a different
# shape from a dictionary. This represents a customer's rental log.
sample_booking = [
    ("Single Kayak", 2),
    ("Life Jacket", 2),
    ("Dry Bag", 1),
]


def calculate_booking_costs(equipment, booking):
    """
    Given the equipment catalogue and a booking (list of (item, hours)
    tuples), return a dictionary like:
    {
        "Single Kayak": {"hours": 2, "rate": 15.00, "cost": 30.00},
        ...
    }
    """
    costs = {}
    for item_name, hours in booking:
        rate = get_rate(equipment, item_name)
        if rate is None:
            # Skip items that aren't in the catalogue rather than crashing.
            continue
        costs[item_name] = {
            "hours": hours,
            "rate": rate,
            "cost": rate * hours,
        }
    return costs


def calculate_total(costs):
    """
    Given the dictionary produced by calculate_booking_costs, return the
    subtotal (sum of all "cost" values).
    """
    return sum(details["cost"] for details in costs.values())


# ===========================================================
# Challenge 3: Tiered Pricing Kata (a standalone function - not tied to
# the booking data structure at all, just plain numbers in and out)
# ===========================================================
def apply_tier_discount(total_hours, subtotal):
    """
    Apply a tiered discount based on total_hours rented across the whole
    booking:
      - 6 or more hours total -> 20% off the subtotal
      - 3 to 5 hours total    -> 10% off the subtotal
      - fewer than 3 hours    -> no discount

    Return a tuple: (discount_amount, description)

    Test it directly with plain numbers, e.g.:
      apply_tier_discount(2, 30.00)  -> (0.0, "No discount ...")
      apply_tier_discount(4, 60.00)  -> (6.0, "10% ...")
      apply_tier_discount(8, 120.00) -> (24.0, "20% ...")
    """
    if total_hours >= 6:
        rate = 0.20
        description = "20% off — booking is 6 hours or more"
    elif total_hours >= 3:
        rate = 0.10
        description = "10% off — booking is 3 to 5 hours"
    else:
        rate = 0.0
        description = "No discount — booking is under 3 hours"

    discount_amount = round(subtotal * rate, 2)
    return discount_amount, description


# ===========================================================
# Challenge 4: Trip Summary Report (with a twist: sort by cost, and
# report the average hourly cost across items - not just a plain receipt)
# ===========================================================
def print_trip_summary(costs, subtotal, discount_amount, discount_description):
    """
    Print a summary that shows:
    - Each item, sorted from HIGHEST cost to LOWEST cost (not input order)
    - The subtotal before discount
    - The discount applied, with its description
    - The final total after discount
    - The average hourly rate across the items in this booking
      (i.e. average of the rate_per_hour values used, not weighted by hours)

    This function should print directly; it doesn't need to return anything.
    """
    print("Trip Summary")
    print("-" * 30)

    # Sort items by cost, highest first.
    sorted_items = sorted(costs.items(), key=lambda pair: pair[1]["cost"], reverse=True)
    for item_name, details in sorted_items:
        print(f"{item_name}: {details['hours']}h @ ${details['rate']:.2f}/h = ${details['cost']:.2f}")

    print("-" * 30)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount_amount:.2f} ({discount_description})")
    final_total = subtotal - discount_amount
    print(f"Total: ${final_total:.2f}")

    if costs:
        average_rate = sum(details["rate"] for details in costs.values()) / len(costs)
        print(f"Average hourly rate: ${average_rate:.2f}")


# ===========================================================
# Interactive booking builder - lets the "customer" type in their own
# booking (item name + hours, repeated until they're done), instead of
# using the hardcoded sample_booking. This is the stretch goal from the
# original comment, now wired in.
# ===========================================================
def build_booking_from_input(equipment):
    """
    Repeatedly ask the user for an item name and number of hours,
    validating both, until they type 'done'. Returns a list of
    (item_name, hours) tuples in the same shape as sample_booking.
    """
    booking = []
    print("Enter items for your booking. Type 'done' when finished.")
    print("Available items:", ", ".join(equipment.keys()))

    while True:
        item_name = input("\nItem name (or 'done'): ").strip()
        if item_name.lower() == "done":
            break

        rate = get_rate(equipment, item_name)
        if rate is None:
            print(f"  '{item_name}' isn't in the catalogue. Try again.")
            continue

        hours_input = input(f"Hours for {item_name}: ").strip()
        try:
            hours = float(hours_input)
            if hours <= 0:
                raise ValueError
        except ValueError:
            print("  Please enter a positive number for hours. Try again.")
            continue

        booking.append((item_name, hours))
        print(f"  Added: {item_name} for {hours} hour(s).")

    return booking


# ===========================================================
# Test harness - run this file to see your functions in action.
# Challenges 1-3 print automatically; Challenge 4 uses a booking you
# type in yourself.
# ===========================================================
if __name__ == "__main__":
    print("--- Challenge 1: Look Up & Filter ---")
    print("Rate for 'Double Kayak':", get_rate(equipment, "Double Kayak"))
    print("Rate for 'Surfboard' (not in catalogue):", get_rate(equipment, "Surfboard"))
    print("Accessories:", list_by_type(equipment, "accessory"))
    print("Most expensive item:", most_expensive_item(equipment))

    print("\n--- Challenge 2: Process a Booking Log (using sample_booking) ---")
    costs = calculate_booking_costs(equipment, sample_booking)
    print("Costs:", costs)
    subtotal = calculate_total(costs)
    print("Subtotal:", subtotal)

    print("\n--- Challenge 3: Tiered Pricing Kata ---")
    print(apply_tier_discount(2, 30.00))
    print(apply_tier_discount(4, 60.00))
    print(apply_tier_discount(8, 120.00))

    print("\n--- Challenge 4: Trip Summary Report (your own booking) ---")
    user_booking = build_booking_from_input(equipment)

    if not user_booking:
        print("\nNo items were booked - nothing to summarise.")
    else:
        user_costs = calculate_booking_costs(equipment, user_booking)
        user_subtotal = calculate_total(user_costs)
        user_total_hours = sum(hours for _, hours in user_booking)
        user_discount_amount, user_discount_description = apply_tier_discount(
            user_total_hours, user_subtotal
        )
        print()
        print_trip_summary(user_costs, user_subtotal, user_discount_amount, user_discount_description)