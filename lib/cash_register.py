#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_item_cost = 0

  def add_item(self, title, price, quantity=1):
        item_cost = price * quantity
        self.items.extend([title] * quantity)
        self.total += item_cost
        self.last_item_cost = item_cost

  def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= int(discount_amount)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

  def void_last_transaction(self):
        if self.items:
            self.total = max(0, self.total - self.last_item_cost)
            self.items.pop()