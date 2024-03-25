class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Move along ..")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle("tesla", "model 3")

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle("Cardilac", "Escalade")
your_car.get_make_model()
my_car.moves()


class Airoplan(Vehicle):
    def __init__(self, make, model, faa_ID):
        super().__init__(make, model)
        self.faa_ID = faa_ID

    def moves(self):
        print("Fly along ...")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along")


class Gulf3(Vehicle):
    pass


cessna = Airoplan("cessna", "hawk", "H-12375V")
buldo_Truck = Truck("Marks", "Granula 04")
golf = Gulf3("Hundai", "Accord")

cessna.get_make_model()
cessna.moves()
buldo_Truck.get_make_model()
buldo_Truck.moves()
golf.get_make_model()
golf.moves()

print("\n\n")
# for loop

for m in (my_car, your_car, golf, cessna, buldo_Truck):
    m.get_make_model()
    m.moves()
