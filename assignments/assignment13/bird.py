# Author: Gatlin Lawson

class Bird:
    def __init__(self, bird_type, color, food, description):
        self.bird_type = bird_type
        self.color = color
        self.food = food
        self.description = description

    def display(self):
        print(f"""
        *** {self.bird_type} ***
        color: {self.color}
        food: {self.food}
        {self.description}
        """)
    
    def is_match(self, bird_name):
        if bird_name == self.bird_type:
            return True
        else:
            return False