class VendingMachine:
    def __init__(self, initial_soda, initial_water, initial_coffee):
        self.soda_count = initial_soda
        self.water_count = initial_water
        self.coffee_count = initial_coffee

    def purchase(self, drink_type):
        if drink_type == 'soda':
            if self.soda_count > 0:
                self.soda_count -= 1
                return f"You have purchased a soda. {self.soda_count} sodas remaining."
            else:
                return "Sorry, we're out of sodas."
        elif drink_type == 'water':
            if self.water_count > 0:
                self.water_count -= 1
                return f"You have purchased a water. {self.water_count} waters remaining."
            else:
                return "Sorry, we're out of water."
        elif drink_type == 'coffee':
            if self.coffee_count > 0:
                self.coffee_count -= 1
                return f"You have purchased a coffee. {self.coffee_count} coffees remaining."
            else:
                return "Sorry, we're out of coffee."
        else:
            return "Invalid drink type."

    def restock(self, drink_type, quantity):
        if drink_type == 'soda':
            self.soda_count += quantity
            return f"{quantity} sodas added. Total sodas now: {self.soda_count}"
        elif drink_type == 'water':
            self.water_count += quantity
            return f"{quantity} waters added. Total waters now: {self.water_count}"
        elif drink_type == 'coffee':
            self.coffee_count += quantity
            return f"{quantity} coffees added. Total coffees now: {self.coffee_count}"
        else:
            return "Invalid drink type."

    def report_inventory(self):
        return f"Soda: {self.soda_count} bottles, Water: {self.water_count} bottles, Coffee: {self.coffee_count} bottles"

# Program
vending_machine = VendingMachine(12, 21, 10)

while True:
    command = input("Enter a command (purchase, restock, report, quit/q to exit): ").lower()

    if command == 'quit' or command == 'q':
        break
    elif command == 'purchase':
        drink_type = input("Enter the drink type (soda, water, coffee): ").lower()
        result = vending_machine.purchase(drink_type)
        print(result)
    elif command == 'restock':
        drink_type = input("Enter the drink type to restock (soda, water, coffee): ").lower()
        quantity = int(input(f"Enter the quantity to restock for {drink_type}: "))
        result = vending_machine.restock(drink_type, quantity)
        print(result)
    elif command == 'report':
        inventory = vending_machine.report_inventory()
        print(inventory)
    else:
        print("Invalid command. Please enter a valid command.")

