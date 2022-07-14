from heroes import SuperHero
from places import Place


class Media:
    def create_news(self, hero: SuperHero, place: Place):
        print(f'{hero.name} saved the {place.name}!')
