# from Inheritance.mix_it_06E.project.parking_mall.parking_mall import ParkingMall
from project.parking_mall.parking_mall import ParkingMall


class Level3(ParkingMall):
    def __init__(self):
        super().__init__(80)
