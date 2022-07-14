from heroes import SuperHero, Superman, ChuckNorris
from places import Place, Tokyo, Kostroma
from antagonistfinder import AntagonistFinder
from media import Media


def save_the_place(hero: SuperHero, place: Place, media: Media):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    media.create_news(hero, place)


if __name__ == '__main__':
    media = Media()

    save_the_place(Superman(), Kostroma(), media)
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo(), media)


