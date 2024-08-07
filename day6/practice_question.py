

# Create a class Equipment that stores
# Eid,Ename,Brand,Total qty,Aval Eqy.
# Add Equipment To stock
# Delete Equipment From stock
# updata the quantity. print the list of Availabe Equipments.
#create a new Dictionary that stores the record of students who take the sports Equipment adn name is as Rental. Dictionary Contains:Name,Rollno
#Eid,Ename,status,Return condition
# Create two function as Rent_item and Return_item
# Rent_item= this function will generate the new Record to the dictionary Rental and fill all the details and mark the condition as good and status as Rented.
# Return_item = this function will mark the status as Returned if student return the item and also mention the condition as (good or Damaged).
import numpy as np
import pandas as pd

class Equipment:

    def __init__(self):
        self.stock = {
            'Eid': [],
            'Ename': [],
            'Brand': [],
            'Total_qty': [],
            'Avail_qty': []
        }
        self.rental = {}  # Dictionary to store rental records

    def add_equipment(self, eid, ename, brand, total_qty):
        self.stock['Eid'].append(eid)
        self.stock['Ename'].append(ename)
        self.stock['Brand'].append(brand)
        self.stock['Total_qty'].append(total_qty)
        self.stock['Avail_qty'].append(total_qty)
        print(f"Equipment {ename} added to stock.")

    def delete_equipment(self, eid):
        try:
            index = self.stock['Eid'].index(eid)
            for key in self.stock.keys():
                self.stock[key].pop(index)
            print(f"Equipment with ID {eid} deleted from stock.")
        except ValueError:
            print("Equipment ID not found.")

    def update_quantity(self, eid, new_qty):
        try:
            index = self.stock['Eid'].index(eid)
            self.stock['Total_qty'][index] = new_qty
            self.stock['Avail_qty'][index] = new_qty
            print(f"Quantity for equipment ID {eid} updated to {new_qty}.")
        except ValueError:
            print("Equipment ID not found.")

    def print_available_equipment(self):
        print("Available Equipment:")
        for i in range(len(self.stock['Eid'])):
            # print(f"ID: {self.stock['Eid'][i]}, Name: {self.stock['Ename'][i]}, Brand: {self.stock['Brand'][i]}, Available Quantity: {self.stock['Avail_qty'][i]}")
            df = pd.DataFrame(self.stock)
            print(df)
            print("\n")
            

    def rent_item(self, name, rollno, eid):
        try:
            index = self.stock['Eid'].index(eid)
            if self.stock['Avail_qty'][index] > 0:
                self.stock['Avail_qty'][index] -= 1
                self.rental[rollno] = {
                    'Name': name,
                    'Eid': eid,
                    'Ename': self.stock['Ename'][index],
                    'Status': 'Rented',
                    'Return_condition': 'Good'
                }
                print(f"Item ID {eid} rented to {name}.")
            else:
                print("No available quantity for this item.")
        except ValueError:
            print("Equipment ID not found.")

    def return_item(self, rollno, condition):
        if rollno in self.rental:
            eid = self.rental[rollno]['Eid']
            index = self.stock['Eid'].index(eid)
            self.stock['Avail_qty'][index] += 1
            self.rental[rollno]['Status'] = 'Returned'
            self.rental[rollno]['Return_condition'] = condition
            print(f"Item ID {eid} returned by {self.rental[rollno]['Name']}. Condition: {condition}.")
        else:
            print("Rental record not found.")

# Example usage:
equip_manager = Equipment()

equip_manager.add_equipment('001', 'Basketball', 'Nike', 10)
equip_manager.add_equipment('002', 'Soccer Ball', 'Adidas', 15)
equip_manager.print_available_equipment()

equip_manager.rent_item('John Doe', '123', '001')
equip_manager.print_available_equipment()

equip_manager.return_item('123', 'Good')
equip_manager.print_available_equipment()

equip_manager.delete_equipment('002')
equip_manager.print_available_equipment()


         
   
 
