class Coordinate:
    __x: int
    __y: int

    def __init__(self, x_coord, y_coord):
        self.__x = x_coord
        self.__y = y_coord

    def distance_from(self, other):
        # TODO: actually calculate distance between the coordinates.
        #       e.g. return abs(self.__x - other.__x)
        return 0
