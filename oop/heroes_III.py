from abc import ABC, abstractmethod

class WeaponDoesNotMatchHero(Exception):
    def __init__(self, weapon_type: str, hero_classname: str) -> None:
        super().__init__(f'Hero class {hero_classname} cannot use weapon with type {weapon_type.type}')

class WeaponTypes:
    types = 'melee', 'range', 'magic'

class WeaponTypeError(Exception):
    def __init__(self, w_type: str):
        super().__init__(f'Weapon type {w_type} is not defined in avaliable types: {WeaponTypes.types}')

class Weapon:
    def __init__(self, title: str, w_type: str) -> None:
        self.title, self.type = title, w_type

    @property
    def type(self) -> str:
        return self._type
    @type.setter
    def type(self, new_type: str) -> None:
        if not isinstance(new_type, str):
            raise TypeError(f'Weapon type expected to be str, not {type(new_type).__name__}')
        if not new_type in WeaponTypes.types:
            raise WeaponTypeError(new_type)
        self._type = new_type

class Hero(ABC):
    melee = range = magic = False
    @abstractmethod
    def __init__(self, name: str, weapon: Weapon):
        self.name, self.weapon = name, weapon

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name} with weapon {self.weapon.title}'

    @property
    def weapon(self) -> Weapon:
        return self._weapon

    @weapon.setter
    def weapon(self, new_weapon: Weapon) -> None:
        if not isinstance(new_weapon, Weapon):
            raise TypeError(f'{self.__class__.__name__} expects weapon to be Weapon instance')
        if not getattr(self, new_weapon.type):
            raise WeaponDoesNotMatchHero(new_weapon, self.__class__.__name__)
        self._weapon = new_weapon

class Melee(Hero):
    melee = True

class Ranged(Hero):
    range = True

class Sorcerer(Hero):
    magic = True

class Necromancer(Sorcerer):
    def __init__(self, name: str, weapon: Weapon):
        super().__init__(name, weapon)

class Elf(Ranged, Sorcerer):
    def __init__(self, name: str, weapon: Weapon):
        super().__init__(name, weapon)

sword, bow, magic = { Weapon('Kyriakos Grizzly', 'melee'),
                     Weapon('Konan', 'range'),
                     Weapon('NecroBand', 'magic')

}

print(Necromancer('Nagash', sword))