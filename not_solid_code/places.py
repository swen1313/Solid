from abc import ABC, abstractmethod


class Place(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def get_antagonist():
        pass


class Kostroma(Place):
    name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    name = 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')
