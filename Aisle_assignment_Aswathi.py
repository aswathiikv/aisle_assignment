#!/usr/bin/env python
# coding: utf-8

# In[8]:


import re,math

class Item():
    
    EXEMPTED = ['food','chocolates','chocolate','pill','medicine','book','books','pills']

    def __init__(self, quantity: int, text: str, price: float):
        self.quantity = quantity
        self.text = text
        self.price = price
        self._compute_tax()

    def _compute_tax(self):
        self.tax_rate = 0.1
        if any(word in self.text for word in Item.EXEMPTED):
            self.tax_rate = 0
        if 'imported' in self.text:
            self.tax_rate += 0.05
        self.tax = math.ceil(self.price*self.tax_rate*20)/20
        self.final_price = round(self.quantity * (self.price + self.tax), 2)

        print(f'{self.quantity} {self.text}: {self.final_price}')


class Receipt():
    
    PATTERN = re.compile('(\d+)\ +([a-zA-Z\ ]+)\ +at\ +(\d+\.\d+)', re.MULTILINE | re.IGNORECASE)

    def __init__(self, free_text: str):
        matches = Receipt.PATTERN.findall(free_text)
        self.items = []
        if len(matches):
            for match in matches:
                quantity, text, price = match
                item = Item(int(quantity), text, float(price))
                self.items.append(item)
            self.total_tax = round(sum([item.tax for item in self.items]), 2)
            self.total_price = round(sum([item.final_price for item in self.items]), 2)

            print('Sales Taxes:', self.total_tax)
            print('Total:', self.total_price)
        else:
            print('No valid items!')

if __name__ == '__main__':
    receipt = Receipt('''1 book at 12.49
    1 music CD at 14.99
    1 chocolate bar at 0.85''')
    print('\n###############################################################\n')

    receipt = Receipt('''1 imported box of chocolates at 10.00 1 imported bottle of perfume at 47.50''')
    print('\n###############################################################\n')

    receipt = Receipt('''1 imported box of perfume at 27.99 1 bottle of perfume at 18.99
    # 1 packet of headache pills at 9.75
    # 1 box of imported chocolates at 11.25''')


# In[ ]:




