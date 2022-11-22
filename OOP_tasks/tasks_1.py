class Point3D:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        self.coordinates = []

    def __del__(self):
        pass

    def get_coord(self):
        return f'coordinates are - {tuple(self.coordinates)}'

    def set_coord(self, lst):
        self.coordinates.clear()
        for x in lst:
            self.coordinates.append(x)


x1 = Point3D()
print(x1.get_coord())
x1.set_coord([3, 5])
print(x1.get_coord())

