class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restauant_name = restaurant_name
        self.cusine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restauant_name)
        print(self.cusine_type)
    def open_restaurant(self):
        print("The restaurant is still open")
        
restaurant_one = Restaurant('hanhan', 'China')
restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()

restaurant_two = Restaurant('dengjia','foregin')
restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()

restaurant_three = Restaurant('huanghaitao', 'English')
restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()
