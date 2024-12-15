print("............DISCOUNT CALCULATOR......................")

def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    price = price - (price * discount_percent/100)
    return print(f"The price for the item is {price}.\nThank you")
  else:
    return print(f"The price for the item is {price}.\nThank you")
  
calculate_discount(price = int(input("Type your price: ")), discount_percent = int(input("Type your discount_percentage: ")))