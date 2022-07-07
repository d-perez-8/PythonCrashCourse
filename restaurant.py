class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        number_served = 0 # This is called an attribute

    def describe_restaurant(self): # This is called a method
        """Prints out 2 pieces of information"""
        print(f"The restuarant's name is {self.restaurant_name}.")
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type}.")
    
    def open_restaurant(self):
        """States whether the restaurant is open"""
        print(f"{self.restaurant_name.title()} is now open!")

    def set_number_served(self, number_served):
        """Initial number of customers served"""
        self.number_served = number_served

    def increment_number_served(self, added_served):
        """Adds number of customers served to number_served"""
        self.number_served += added_served