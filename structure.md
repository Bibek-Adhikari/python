# py.py — Structure and Documentation

Overview
--------
py.py contains four separate practice challenges (Skill Builders) for working with small Python programs that manipulate a rental equipment catalogue and simple booking data. Each challenge is implemented as independent, self-contained functions so they can be run and tested individually.

File purpose
------------
- Provide small, testable exercises related to: lookup and filtering in a nested dictionary, processing booking logs, applying tiered discounts, and printing a trip summary.
- Run as a script to exercise the functions interactively or with the provided sample booking data.

Top-level data
--------------
- equipment: dict
  - A catalogue mapping item name (str) -> details (dict) with keys:
    - rate_per_hour: float
    - type: str (e.g., "watercraft", "accessory", "safety gear")
  - Example item: "Single Kayak": {"rate_per_hour": 15.00, "type": "watercraft"}

Functions (by challenge)
------------------------
Challenge 1 — Look Up & Filter
- get_rate(equipment, item_name) -> float | None
  - Returns the hourly rate for a named item, or None if the item is not present.
  - Uses a simple dictionary lookup.

- list_by_type(equipment, type_name) -> list[str]
  - Returns a list of item names whose details["type"] equals type_name.
  - Order is not guaranteed.

- most_expensive_item(equipment) -> tuple[str, float]
  - Returns (name, rate) for the item with the highest rate_per_hour.
  - Uses max() with a key that reads rate_per_hour.

Challenge 2 — Process a Booking Log
- calculate_booking_costs(equipment, booking) -> dict
  - booking: list of tuples (item_name, hours)
  - Returns a mapping item_name -> {"hours": hours, "rate": rate, "cost": rate * hours}
  - Items not present in the catalogue are skipped (silently).

- calculate_total(costs) -> float
  - Sums the "cost" values in the costs dict and returns the subtotal.

Challenge 3 — Tiered Pricing Kata
- apply_tier_discount(total_hours, subtotal) -> tuple[float, str]
  - Applies a tiered discount based on total_hours across the booking:
    - 6+ hours: 20% off
    - 3–5 hours: 10% off
    - <3 hours: 0% off
  - Returns (discount_amount, description) where discount_amount is rounded to 2 decimals.

Challenge 4 — Trip Summary Report
- print_trip_summary(costs, subtotal, discount_amount, discount_description) -> None
  - Prints a human-readable summary including:
    - Each booked item sorted from highest cost to lowest
    - Subtotal, discount line with description, final total
    - Average hourly rate across the items (unweighted average of the per-item rates)

Interactive helper
- build_booking_from_input(equipment) -> list[tuple[str, float]]
  - CLI helper that prompts the user to enter item names and hours until they enter "done".
  - Validates item exists and hours is a positive number.

Script entrypoint
-----------------
- When run as __main__, the file demonstrates:
  1. Challenge 1 outputs (lookup, list_by_type, most_expensive_item).
  2. Challenge 2 using a hardcoded sample_booking and subtotal calculation.
  3. Challenge 3 with example calls.
  4. Challenge 4 by prompting the user to build a booking interactively and then printing the trip summary.

Usage
-----
- Run the script directly in a console:
  python py.py

- To run specific functions from an interactive session or tests, import them:
  from py import get_rate, calculate_booking_costs, apply_tier_discount

Example flow (non-interactive):
- Use the provided sample_booking to compute costs and subtotal:
  costs = calculate_booking_costs(equipment, sample_booking)
  subtotal = calculate_total(costs)
  discount_amount, desc = apply_tier_discount(sum(h for _, h in sample_booking), subtotal)
  print_trip_summary(costs, subtotal, discount_amount, desc)

Testing notes
-------------
- Functions are small and pure (no side effects) except for build_booking_from_input and print_trip_summary which interact with stdin/stdout. Prefer testing pure functions directly.
- Example assertions to include in unit tests:
  - get_rate(equipment, "Single Kayak") == 15.0
  - list_by_type(equipment, "accessory") contains "Dry Bag"
  - most_expensive_item(equipment)[0] in equipment
  - calculate_total(calculate_booking_costs(equipment, sample_booking)) == expected subtotal
  - apply_tier_discount(4, 60.00) -> (6.0, "10% off") (or contains the text description)

Notes and suggestions
---------------------
- calculate_booking_costs currently skips unknown items; consider returning an "errors" list if callers need to know about missing items.
- Average hourly rate computed in print_trip_summary is an unweighted average of per-item rates; if a weighted average is desired (weighted by hours), change the formula accordingly.

This document is intended to be a concise developer-facing reference for py.py. If more detail or example unit tests are required, say which functions to focus on and a small test suite will be added.
