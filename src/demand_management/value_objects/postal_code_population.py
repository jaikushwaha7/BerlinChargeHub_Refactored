from dataclasses import dataclass

@dataclass
class PostalCodePopulation:
    """
    Represents a charging station with location information.
    """
    def __init__(self, value: int):
        self._value = value

    def value(self):
        return self._value



