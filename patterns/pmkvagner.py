class Musican:
    available_roles = 'Drummer', 'Vocalist', 'Guitarist', 'Keys'
    def __init__(self, name: str, role: str) -> None:
        self.name, self.role = name, role

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, new_role: str) -> None:
        if not isinstance(new_role, str):
            raise TypeError(f'{new_role} must be str, not {type(new_role).__name__}')
        if new_role not in self.available_roles:
            raise ValueError(f'{new_role} is not in available roles, our roles: {self.available_roles}')
        self._role = new_role

    def play(self, piece: str) -> str:
        print(f'{self.__class__.__name__} sing a {piece}')

class Song:
    def __init__(self, title: str, parts: list[dict[str, str]]) -> None:
        self.parts = parts
        self.title = title

    @property
    def parts(self) -> list[dict[str, str]]:
        return self._parts
    
    @parts.setter
    def parts(self, new_parts: list[dict[str, str]]) -> None:
        if not (isinstance(new_parts, list) and all([isinstance(part, dict) for part in new_parts])):
            raise TypeError(f'Parts should be list of dicts')
        for part in new_parts:
            for role in part.keys():
                if not role in Musican.available_roles:
                    raise ValueError(f'{role} role is not available')
        self._parts = new_parts
    

        