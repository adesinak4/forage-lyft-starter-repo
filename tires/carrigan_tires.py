from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_a, tire_b, tire_c, tire_d):
        self.tire_a = tire_a
        self.tire_b = tire_b
        self.tire_c = tire_c
        self.tire_d = tire_d

    def needs_service(self):
        if self.tire_a >= 0.9 or self.tire_b >= 0.9 or self.tire_c >= 0.9 or self.tire_d >= 0.9:
            return True
        else:
            return False
