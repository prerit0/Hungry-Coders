# Create a shopping bill calculator. Use variables for 3 items with their prices and quantities. Calculate subtotal, apply 10% tax, and display a detailed bill with f-strings.

price_apple = 2.00
price_bread = 2.00
price_milk = 3.50

qty_apple = 3
qty_bread = 2
qty_milk = 1

apple_total = price_apple*qty_apple   
bread_total = price_bread*qty_bread
milk_total = price_milk*qty_milk

Subtotal = apple_total+bread_total+milk_total``
Tax = Subtotal*0.10
Total = Subtotal+Tax

print("=== SHOPPING BILL ===")
print(f"Item 1: Apple x 3 = ${apple_total:.2f}")
print(f"Item 2: Bread x 2 = ${bread_total:.2f}")
print(f"Item 3: Milk x 1 = ${milk_total:.2f}")
print(f"Subtotal: ${Subtotal:.2f}")
print(f"Tax (10%): ${Tax:.2f}")
print(f"Total: ${Total:.2f}")

# Hint
# Item total = price * quantity. Tax = subtotal * 0.10. Final = subtotal + tax.

# Python Note
# Use f"{price:.2f}" to format numbers as currency with 2 decimal places

# Expected Output (example)
# === SHOPPING BILL ===
# Item 1: Apple × 3 = $6.00
# Item 2: Bread × 2 = $4.00
# Item 3: Milk × 1 = $3.50
# Subtotal: $13.50
# Tax (10%): $1.35
# Total: $14.85