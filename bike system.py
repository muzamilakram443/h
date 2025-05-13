class Bike:
    def __init__(self, brand, model, engine_cc, color):
        self.brand = brand
        self.model = model
        self.engine_cc = engine_cc
        self.color = color

    def assemble(self):
        print(f"Assembling {self.color} {self.brand} {self.model} ({self.engine_cc}cc)...")

    def paint(self, new_color):
        print(f"Painting the bike {new_color}...")
        self.color = new_color

    def test_ride(self):
        print(f"Test riding the {self.brand} {self.model}...")

    def display_specs(self):
        print(f"--- Bike Specifications ---")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Engine: {self.engine_cc}cc")
        print(f"Color: {self.color}")
        print("---------------------------")


# Example usage
def make_bike():
    bike1 = Bike("Yamaha", "R15 V4", 155, "Blue")
    bike1.assemble()
    bike1.paint("Matte Black")
    bike1.test_ride()
    bike1.display_specs()

    print("\nMaking another bike...\n")

    bike2 = Bike("Honda", "CBR500R", 500, "Red")
    bike2.assemble()
    bike2.test_ride()
    bike2.display_specs()

make_bike()
