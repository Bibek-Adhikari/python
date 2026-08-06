"""
Skill Builders: Riverside Kayak Rentals
------------------------------------------------
STARTER CODE. Complete the 4 functions marked TODO below.

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
    # TODO: implement
    pass


def list_by_type(equipment, type_name):
    """
    Return a list of item names whose "type" matches type_name.
    e.g. list_by_type(equipment, "accessory") -> ["Dry Bag", "Waterproof Phone Case"]
    (order doesn't matter)
    """
    # TODO: implement
    pass


def most_expensive_item(equipment):
    """
    Return a tuple (name, rate) for the item with the highest rate_per_hour.
    """
    # TODO: implement
    pass


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
    # TODO: implement
    pass


def calculate_total(costs):
    """
    Given the dictionary produced by calculate_booking_costs, return the
    subtotal (sum of all "cost" values).
    """
    # TODO: implement
    pass


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
    # TODO: implement
    pass


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
    # TODO: implement
    pass


# ===========================================================
# Test harness - run this file to see your functions in action.
# No input() needed for Challenges 1-3.
# ===========================================================
if __name__ == "__main__":
    print("--- Challenge 1: Look Up & Filter ---")
    print("Rate for 'Double Kayak':", get_rate(equipment, "Double Kayak"))
    print("Rate for 'Surfboard' (not in catalogue):", get_rate(equipment, "Surfboard"))
    print("Accessories:", list_by_type(equipment, "accessory"))
    print("Most expensive item:", most_expensive_item(equipment))

    print("\n--- Challenge 2: Process a Booking Log ---")
    costs = calculate_booking_costs(equipment, sample_booking)
    print("Costs:", costs)
    subtotal = calculate_total(costs)
    print("Subtotal:", subtotal)

    print("\n--- Challenge 3: Tiered Pricing Kata ---")
    print(apply_tier_discount(2, 30.00))
    print(apply_tier_discount(4, 60.00))
    print(apply_tier_discount(8, 120.00))

    print("\n--- Challenge 4: Trip Summary Report ---")
    total_hours = sum(hours for _, hours in sample_booking)
    discount_amount, discount_description = apply_tier_discount(total_hours, subtotal)
    print_trip_summary(costs, subtotal, discount_amount, discount_description)

    # --- Optional stretch (not required) ---
    # Once all 4 challenges work, try wrapping them in your own input()-driven
    # loop so a "customer" can build their own booking interactively. This
    # step is closer to what Assessment 2 asks for, but it's optional here.
