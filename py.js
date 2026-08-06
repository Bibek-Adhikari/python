/**
 * Skill Builders: Riverside Kayak Rentals
 * ------------------------------------------------
 * All 4 functions implemented.
 * 
 * Unlike a full checkout program, these are 4 SEPARATE, self-contained
 * challenges. Each one exercises a skill you'll need for Assessment 2,
 * but none of them ask you to build one continuous input-driven program.
 * Run this file directly (no typing needed) and check the printed output
 * against the expected results noted in the practice activity doc.
 */

// Equipment catalogue - an object (similar to Python dict)
const equipment = {
    "Single Kayak":          { rate_per_hour: 15.00, type: "watercraft" },
    "Double Kayak":          { rate_per_hour: 25.00, type: "watercraft" },
    "Stand-Up Paddleboard":  { rate_per_hour: 12.00, type: "watercraft" },
    "Life Jacket":           { rate_per_hour: 3.00,  type: "safety gear" },
    "Dry Bag":               { rate_per_hour: 2.00,  type: "accessory" },
    "Waterproof Phone Case": { rate_per_hour: 1.50,  type: "accessory" },
};

// ===========================================================
// Challenge 1: Look Up & Filter
// ===========================================================

/**
 * Return the hourly rate for item_name, or null if it isn't in the catalogue.
 */
function getRate(equipment, itemName) {
    if (equipment.hasOwnProperty(itemName)) {
        return equipment[itemName].rate_per_hour;
    }
    return null;
}

/**
 * Return a list of item names whose "type" matches typeName.
 * e.g. listByType(equipment, "accessory") -> ["Dry Bag", "Waterproof Phone Case"]
 * (order doesn't matter)
 */
function listByType(equipment, typeName) {
    return Object.keys(equipment).filter(name => equipment[name].type === typeName);
}

/**
 * Return an object { name, rate } for the item with the highest rate_per_hour.
 */
function mostExpensiveItem(equipment) {
    let maxName = null;
    let maxRate = -Infinity;
    for (const [name, details] of Object.entries(equipment)) {
        if (details.rate_per_hour > maxRate) {
            maxRate = details.rate_per_hour;
            maxName = name;
        }
    }
    return { name: maxName, rate: maxRate };
}

// ===========================================================
// Challenge 2: Process a Booking Log
// ===========================================================

// A booking is given as an array of [itemName, hours] pairs.
const sampleBooking = [
    ["Single Kayak", 2],
    ["Life Jacket", 2],
    ["Dry Bag", 1],
];

/**
 * Given the equipment catalogue and a booking (array of [item, hours] pairs),
 * return an object like:
 * {
 *   "Single Kayak": { hours: 2, rate: 15.00, cost: 30.00 },
 *   ...
 * }
 */
function calculateBookingCosts(equipment, booking) {
    const costs = {};
    for (const [itemName, hours] of booking) {
        const rate = getRate(equipment, itemName);
        if (rate === null) {
            // Skip items that aren't in the catalogue rather than crashing.
            continue;
        }
        costs[itemName] = {
            hours: hours,
            rate: rate,
            cost: rate * hours,
        };
    }
    return costs;
}

/**
 * Given the object produced by calculateBookingCosts, return the subtotal
 * (sum of all "cost" values).
 */
function calculateTotal(costs) {
    let total = 0;
    for (const details of Object.values(costs)) {
        total += details.cost;
    }
    return total;
}

// ===========================================================
// Challenge 3: Tiered Pricing Kata
// ===========================================================

/**
 * Apply a tiered discount based on totalHours rented across the whole booking:
 *   - 6 or more hours total -> 20% off the subtotal
 *   - 3 to 5 hours total    -> 10% off the subtotal
 *   - fewer than 3 hours    -> no discount
 *
 * Return an object: { discountAmount, description }
 *
 * Test it directly with plain numbers, e.g.:
 *   applyTierDiscount(2, 30.00)  -> { discountAmount: 0.0, description: "No discount ..." }
 *   applyTierDiscount(4, 60.00)  -> { discountAmount: 6.0, description: "10% ..." }
 *   applyTierDiscount(8, 120.00) -> { discountAmount: 24.0, description: "20% ..." }
 */
function applyTierDiscount(totalHours, subtotal) {
    let rate, description;
    if (totalHours >= 6) {
        rate = 0.20;
        description = "20% off — booking is 6 hours or more";
    } else if (totalHours >= 3) {
        rate = 0.10;
        description = "10% off — booking is 3 to 5 hours";
    } else {
        rate = 0.0;
        description = "No discount — booking is under 3 hours";
    }

    // Round to 2 decimal places
    const discountAmount = Math.round(subtotal * rate * 100) / 100;
    return { discountAmount, description };
}

// ===========================================================
// Challenge 4: Trip Summary Report
// ===========================================================

/**
 * Print a summary that shows:
 * - Each item, sorted from HIGHEST cost to LOWEST cost (not input order)
 * - The subtotal before discount
 * - The discount applied, with its description
 * - The final total after discount
 * - The average hourly rate across the items in this booking
 *   (i.e. average of the rate_per_hour values used, not weighted by hours)
 *
 * This function prints directly; it doesn't return anything.
 */
function printTripSummary(costs, subtotal, discountAmount, discountDescription) {
    console.log("Trip Summary");
    console.log("-".repeat(30));

    // Sort items by cost, highest first.
    const sortedItems = Object.entries(costs).sort((a, b) => b[1].cost - a[1].cost);
    for (const [itemName, details] of sortedItems) {
        console.log(
            `${itemName}: ${details.hours}h @ $${details.rate.toFixed(2)}/h = $${details.cost.toFixed(2)}`
        );
    }

    console.log("-".repeat(30));
    console.log(`Subtotal: $${subtotal.toFixed(2)}`);
    console.log(`Discount: -$${discountAmount.toFixed(2)} (${discountDescription})`);
    const finalTotal = subtotal - discountAmount;
    console.log(`Total: $${finalTotal.toFixed(2)}`);

    const costKeys = Object.keys(costs);
    if (costKeys.length > 0) {
        let sumRates = 0;
        for (const key of costKeys) {
            sumRates += costs[key].rate;
        }
        const averageRate = sumRates / costKeys.length;
        console.log(`Average hourly rate: $${averageRate.toFixed(2)}`);
    }
}

// ===========================================================
// Interactive booking builder (Node.js readline version)
// ===========================================================

const readline = require('readline');

function buildBookingFromInput(equipment) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const booking = [];
    console.log("Enter items for your booking. Type 'done' when finished.");
    console.log("Available items:", Object.keys(equipment).join(", "));

    // We'll use a promise-based approach to handle asynchronous input.
    return new Promise((resolve) => {
        const promptUser = () => {
            rl.question("\nItem name (or 'done'): ", (itemName) => {
                itemName = itemName.trim();
                if (itemName.toLowerCase() === "done") {
                    rl.close();
                    resolve(booking);
                    return;
                }

                const rate = getRate(equipment, itemName);
                if (rate === null) {
                    console.log(`  '${itemName}' isn't in the catalogue. Try again.`);
                    promptUser();
                    return;
                }

                rl.question(`Hours for ${itemName}: `, (hoursInput) => {
                    hoursInput = hoursInput.trim();
                    const hours = parseFloat(hoursInput);
                    if (isNaN(hours) || hours <= 0) {
                        console.log("  Please enter a positive number for hours. Try again.");
                        promptUser();
                        return;
                    }

                    booking.push([itemName, hours]);
                    console.log(`  Added: ${itemName} for ${hours} hour(s).`);
                    promptUser();
                });
            });
        };

        promptUser();
    });
}

// ===========================================================
// Test harness - run this file to see your functions in action.
// ===========================================================

async function main() {
    console.log("--- Challenge 1: Look Up & Filter ---");
    console.log("Rate for 'Double Kayak':", getRate(equipment, "Double Kayak"));
    console.log("Rate for 'Surfboard' (not in catalogue):", getRate(equipment, "Surfboard"));
    console.log("Accessories:", listByType(equipment, "accessory"));
    console.log("Most expensive item:", mostExpensiveItem(equipment));

    console.log("\n--- Challenge 2: Process a Booking Log (using sample_booking) ---");
    const costs = calculateBookingCosts(equipment, sampleBooking);
    console.log("Costs:", costs);
    const subtotal = calculateTotal(costs);
    console.log("Subtotal:", subtotal);

    console.log("\n--- Challenge 3: Tiered Pricing Kata ---");
    console.log(applyTierDiscount(2, 30.00));
    console.log(applyTierDiscount(4, 60.00));
    console.log(applyTierDiscount(8, 120.00));

    console.log("\n--- Challenge 4: Trip Summary Report (your own booking) ---");
    const userBooking = await buildBookingFromInput(equipment);

    if (userBooking.length === 0) {
        console.log("\nNo items were booked - nothing to summarise.");
    } else {
        const userCosts = calculateBookingCosts(equipment, userBooking);
        const userSubtotal = calculateTotal(userCosts);
        let totalHours = 0;
        for (const [, hours] of userBooking) {
            totalHours += hours;
        }
        const { discountAmount, description } = applyTierDiscount(totalHours, userSubtotal);
        console.log();
        printTripSummary(userCosts, userSubtotal, discountAmount, description);
    }
}

// Run the main function if this script is executed directly (not imported as module)
if (require.main === module) {
    main();
}