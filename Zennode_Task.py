products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

discount_rules = {
    "flat_10_discount": (200, 10),
    "bulk_5_discount": (10, 0.05),
    "bulk_10_discount": (20, 0.10),
    "tiered_50_discount": (30, 0.50)
}

gift_wrap_fee = 1
shipping_fee = 5

quantities = {}
gift_wraps = {}
for product in products.keys():
    quantity = int(input(f"Enter the quantity of {product}: "))
    wrap = input(f"Is {product} wrapped as a gift? (yes/no): ").lower()
    quantities[product] = quantity
    gift_wraps[product] = wrap == "yes"

product_totals = {}
for product, price in products.items():
    product_totals[product] = quantities[product] * price

subtotal = sum(product_totals.values())
applicable_discounts = {}
discount_price = {}
for rule, (threshold, discount) in discount_rules.items():
    if subtotal >= threshold:
        if rule == "flat_10_discount" :
            applicable_discounts[rule] = subtotal - discount
            discount_price[rule] = discount

        elif rule == "bulk_5_discount" :
            discount_bulk = {}
            temp =0
            for product, price in product_totals.items():
                if quantities[product] > 10 :
                    temp = temp + (price * 5 / 100)
                    discount_bulk[product] = price - (price * 5 / 100)
                else :
                    discount_bulk[product] = price
            discount_price[rule] = temp
            discount = sum(discount_bulk.values())
            applicable_discounts[rule] = discount

        elif rule == "bulk_10_discount" :
            tot = 0
            for quantity in quantities.values() :
                tot = tot + quantity
            if tot > 20 :
                discount_price[rule] = subtotal * 10 / 100
                discount = subtotal - (subtotal * 10 / 100)
            else:
                discount = subtotal
            applicable_discounts[rule] = discount

        elif rule == "tiered_50_discount" :
            tot = 0
            temp = 0
            discount_tiered = {}
            for quantity in quantities.values():
                tot = tot + quantity
            for product, price in product_totals.items():
                if tot >30 and quantities[product]>15 :
                    temp = temp + (price * 50 / 100)
                    discount_tiered[product] = price - (price * 50 / 100)
                else:
                    discount_tiered[product] = price
                discount = sum(discount_tiered.values())
            discount_price[rule] = temp
            applicable_discounts[rule] = discount

if applicable_discounts:
    best_discount_rule = min(applicable_discounts, key=applicable_discounts.get)
    discount_amount = applicable_discounts[best_discount_rule]
    discount_name = best_discount_rule
    discount_got = discount_price[best_discount_rule]
    discounted_subtotal = discount_amount
else:
    discount_name = "No discount applied"
    discounted_subtotal = subtotal

total_units = sum(quantities.values())
shipping_packages = total_units // 10
if total_units % 10 == 0 :
    shipping_fee_total = shipping_packages * shipping_fee
else:
    shipping_fee_total = shipping_packages * shipping_fee + 5

gift_wrap_total = sum([gift_wrap_fee * quantity for product, quantity in quantities.items() if gift_wraps[product]])

total = discounted_subtotal + shipping_fee_total + gift_wrap_total

print("Product Details:")
for product, quantity in quantities.items():
    print(f"{product}: {quantity} x ${products[product]} = ${product_totals[product]}")
print(f"Subtotal: ${subtotal}")
print(f"Discount Applied: {discount_name} {discount_got} $")
print(f"Subtotal With Discount: {discounted_subtotal}")
print(f"Shipping Fee: ${shipping_fee_total}")
print(f"Gift Wrap Fee: ${gift_wrap_total}")
print(f"Total: ${total}")
