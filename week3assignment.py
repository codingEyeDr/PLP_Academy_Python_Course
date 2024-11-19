# Question 1

def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount.

  Args:
    price: The original price.
    discount_percent: The discount percentage.

  Returns:
    The final price after applying the discount, or the original price if the
    discount is less than 20%.
  """
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Example usage:
original_price = 100
discount = 25

final_price = calculate_discount(original_price, discount)
print(f"Original Price: ${original_price:.2f}")
print(f"Discount: {discount}%")
print(f"Final Price: ${final_price:.2f}")



# Question 2

def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount.

  Args:
    price: The original price.
    discount_percent: The discount percentage.

  Returns:
    The final price after applying the discount, or the original price if the
    discount is less than 20%.
  """
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Get user input
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Print the result
if final_price != original_price:
  print(f"Original Price: ${original_price:.2f}")
  print(f"Discount: {discount_percent}%")
  print(f"Final Price: ${final_price:.2f}")
else:
  print("No discount applied. Original price: $", original_price)