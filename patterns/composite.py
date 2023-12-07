from copy import deepcopy
from typing import Self

class PlayerNotInTeam(Exception):
    pass

class Player:
    def __init__(self, name: str, age: int) -> None:
        self.name, self.age = name, age

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        if not isinstance(new_age, int):
            raise TypeError(f'Age must be int, not {type(new_age).__name__}')
        if new_age < 0:
            raise ValueError(f'Age must be positive')
        self._age = new_age

    def play(self) -> None:
        print(f'{self.__class__.__name__} {self.name} is playing')

    def __str__(self) -> str:
        return f'{self.__class__.__name__}, Name: {self.name}, Age: {self.age}'


class Team:
    def __init__(self, title: str, players: list[Player]) -> None:
        self.title, self.players = title, players
        self._players_counter = 0
        self._set_state()

    def _set_state(self):
        self._state = deepcopy(self.players)

    def reset(self):
        self.players = deepcopy(self._state)
        self._players_counter = 0

    @property
    def players(self) -> list[Player]:
        return self._players

    @staticmethod
    def _check_player(player: Player) -> None:
        if not isinstance(player, Player):
            raise TypeError(f'{player} must be Player, not {type(player).__name__}')

    @players.setter
    def players(self, new_players: list[Player]) -> None:
        for player in new_players:
            self._check_player(player)
        self._players = new_players

    def add_player(self, player: Player) -> None:
        self._check_player(player)
        self.players.append(player)

    def remove_player(self, player: Player) -> None:
        self._check_player(player)
        if player not in self.players:
            raise PlayerNotInTeam(f'{player} is not in the team {self.title}')
        self.players.remove(player)

    def play(self) -> None:
        for player in self.players:
            player.play()

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> Player:
        if self._players_counter >= len(self.players):
            self._players_counter = 0
            raise StopIteration
        self._players_counter += 1
        return self.players[self._players_counter - 1]
