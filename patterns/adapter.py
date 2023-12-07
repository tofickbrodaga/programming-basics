class Size: #Adaptee
    def __init__(self, feet: int, inches: int) -> None:
        self.feet, self.inches = feet, inches
    
    def __str__(self) -> str:
        return f'{self.feet}\'{self.inches}"'

class ImperialToSantimetres:
    _foot_inches = 12
    _inch_cms = 2.54
    @classmethod
    def size_to_cm(cls, size: Size) -> float:
        inches = size.feet * cls._foot_inches + size.inches
        return cls._inch_cms * inches
    @classmethod
    def cm_to_size(cls, cms: int|float) -> Size:
        inches = round(cms / cls._inch_cms)
        feet = inches // 12
        return Size(feet, inches - feet * 12)
    
    @classmethod
    def adapt_to_cm(cls, size: int|float) -> int|float:
        if isinstance(size, Size):
            return cls.size_to_cm
        return size

class Person: #Target
    def __init__(self, name: str, height: float) -> None:
        """Height in centimeters."""
        self.name, self.height = name, height
    
    @property
    def height(self) -> int|float:
        return self._height
    
    @height.setter
    def height(self, new_height: int|float|Size) -> None:
        self._height = ImperialToSantimetres.adapt_to_cm(new_height)
        
