class PlayerNotAdult(Exception):
    pass

class Footballer():
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
class Team:
    def __init__(self, players: list[Footballer]) -> None:
        self.players = players
    @property
    def players(self) -> list[Footballer]:
        return self.__players
    
    @players.setter
    def players(self, new_players: list[Footballer]) -> None:
        if len(new_players) != 11:
            raise ValueError(f'There must be 11 players, youre have a {len(new_players)}')
        for player in new_players:
            if not isinstance(player, Footballer):
                raise TypeError(f'Player must be Footballer, not {type(player)}')
        for player in new_players:
            if player.age < 18:
                raise PlayerNotAdult(f'Упс попался по 228')
        self.__footballer = new_players

egorka = Footballer('Egorka', 18)
egorkins = Team([egorka] * 11)
