class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restauant_name = restaurant_name
        self.cusine_type = cuisine_type
        self.number_serverd = 0
    def describe_restaurant(self):
        print(self.restauant_name)
        print(self.cusine_type)
    def open_restaurant(self):
        print("The restaurant is still open")
    def set_name_served(self, people):
        self.number_serverd = people
    def increment_number_served(self, number_people):
        self.number_serverd += number_people

restaurant = Restaurant('hanhan', 'America')
print(restaurant.number_serverd)
restaurant.set_name_served(20)
print(restaurant.number_serverd)
restaurant.increment_number_served(10)
print(restaurant.number_serverd)