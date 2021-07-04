from Coordinate import Coordinate

MESSAGE_RANGE = 1000


class Shouty:
    __locations: {str: Coordinate}  # person-name -> person's-location
    __shouts: {str: [str]}          # shouter's-name -> list-of-their-messages

    def __init__(self):
        self.__locations = {}
        self.__shouts = {}

    def set_location(self, person: str, location: Coordinate):
        self.__locations[person] = location

    def shout(self, shouter: str, shout: str):
        if shouter not in self.__shouts:
            self.__shouts[shouter] = []
        self.__shouts[shouter].append(shout)

    def get_shouts_heard_by(self, listener: str):
        shouts_heard = {}
        for shouter in iter(self.__shouts):
            persons_shouts: [str] = self.__shouts[shouter]
            distance = self.__locations[listener].distance_from(self.__locations[shouter])
            if distance < MESSAGE_RANGE:
                shouts_heard[shouter] = persons_shouts

        return shouts_heard
