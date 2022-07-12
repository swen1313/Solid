from mixin import *
from abc import ABC, abstractmethod
from antagonistfinder import AntagonistFinder



class TV:
    def create_news(self: 'SuperHero', place):
        place_name = getattr(place, 'name', 'place')
        print(f'{self.name} saved the {place_name}!')

    def create_news_for_planets(self: 'SuperHero', place):
        coordinate_list = getattr(place, 'coordinates', [])
        if coordinate_list:
            for coordinate in coordinate_list:
                print(f'Planet with coordinates {coordinate} was saved by {self..name}')


class SuperHero(ABC):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def ultimate(self):
        pass


class Superman(LaserMixin, PunchMixin, SuperHero):

    def __init__(self):
        super().__init__('Clark Kent', True)

    def attack(self):
        self.punch()

    def ultimate(self):
        self.incinerate_with_lasers()


class ChuckNorris(KickMixin, GunMixin, SuperHero):

    def __init__(self):
        super().__init__('Chuck Norris', False)

    def attack(self):
        self.roundhouse_kick()

    def ultimate(self):
        self.fire_a_gun()

