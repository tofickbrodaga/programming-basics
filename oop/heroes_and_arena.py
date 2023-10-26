# # Hero:
# attrs: health: float|int, weapon: Optional[Weapon], attack: int| float = 10

# Weapon:
# attrs: label, damage int|float

# Arena
# attrs:
# heroes: list[Hero]
# methods:
# pvp( fst_hero: Hero, snd_Hero: Hero) -> int [-1, 0, 1]
# league() -> None

from typing import Any, Self, Optional
import random

class HeroNotFoundError(Exception):
    pass

def check_positive_int(value: Any, classes) -> None:
        if not isinstance(value, classes):
            raise TypeError(f'{type(value).__name__} is not a {classes}')
        if value < 0:
            raise ValueError(f'Value {value} is less than zero')

class Weapon:
    def __init__ (self, label: str, damage: int|float):
        self.label, self.damage = label, damage
    
    @property
    def damage(self) -> int|float:
        return self.__damage
    
    @damage.setter
    def damage(self, new_damage: int|float) -> None:
        check_positive_int(new_damage)
        self.__damage = new_damage

class Hero:
     def __init__(self, name: str,  weapon: Optional[Weapon] = None, health: int|float = 100, attack: int|float = 10):
        self.name, self.weapon, self.health, self.__attack = name, weapon, health, attack

        @property
        def weapon(self) -> Weapon:
            return self.__weapon
        
        @weapon.setter
        def weapon(self, new_weapon = Weapon) -> None:
            if not new_weapon:
                self.__weapon = None
                return 
            if not isinstance(new_weapon, Weapon):
                raise TypeError(f'{type(new_weapon).__name__} is not a Weapon inst')
            self.__weapon = weapon
        
        @property
        def health(self) -> int:
            return self._health
        
        @health.setter
        def health(self, new_health: int) -> None:
            check_positive_int(new_health, (int, ))
            self._health = new_health
        
        @property
        def damage(self) -> int|float:
            attack_dmg = self.weapon.damage if self.weapon else self.__attack
            delta = attack_dmg // 10
            return attack_dmg + random.uniform(-delta, delta)
        
        def pvp(self, other: Self) -> int:
            if not isinstance(other, type(self)):
                raise TypeError(f'{self.name} cannot fight {type(other).__name__}')
            
            hero_hp, other_hp = self.health, other.health
            while hero_hp > 0 and other_hp > 0:
                hero_hp -= other.damage
                other_hp -= self.damage

            if hero_hp <= 0 and other_hp <= 0:
                return 0
            elif hero_hp <= 0:
                return 1
            else:
                return -1
            


class Arena:
    def __init__(self, heroes: list[Hero]):
        self.heroes = heroes
    
    def check_hero(self, hero: Hero) -> None:
         if not isinstance(hero, Hero):
                raise TypeError(f'{type(hero).__name__} is not a Hero')

    @property
    def heroes(self) -> list[Hero]:
        return self._heroes
    
    @heroes.setter
    def heroes(self, new_heroes: list[Hero]) -> None:
        for hero in new_heroes:
            self.check_hero(hero)
        self._heroes = new_heroes
    
    def add_hero(self, hero: Hero):
        self.check_hero(hero)
        self._heroes.append(hero)
    def remove_hero(self, hero: Hero) -> None:
        self.check_hero(hero)
        if hero not in self._heroes:
            raise HeroNotFoundError(f'Hero {hero.name} was not found')
        self._heroes.remove(hero)
        

        

