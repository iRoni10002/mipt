class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def vector2d(cls, x, y):
        return cls(x, y, 0)

    def __str__(self):
        return 'x: {}, y: {}, z: {}'.format(self.x, self.y, self.z)

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    def __mul__(self, other):
        return (self.x * other.x + self.y * other.y + self.z * other.z)

    def __matmul__(self, other):
        ax, bx = self.x, other.x
        ay, by = self.y, other.y
        az, bz = self.z, other.z
        return Vector((ay*bz - az*by), (az*bx - ax*bz), (ax*by - ay*bx))


N = int(input())
points = []
for i in range(N):
    point = tuple(map(int, input().split(' ')))
    if len(point) == 2:
        points.append(Vector.vector2d(point[0], point[1]))
    else:
        points.append(Vector(point[0], point[1], point[2]))

#----- #2 -----#
max = 0
max_vector = Vector(0, 0, 0)
for p in points:
    if abs(p) > max:
        max, max_vector = abs(p), p
print('координаты наиболее удаленной точки:', max_vector)

#----- #3 -----#
centroid = (sum([p.x for p in points]) / len(points),
            sum([p.y for p in points]) / len(points),
            sum([p.z for p in points]) / len(points))
print('Координаты центра масс:', Vector(centroid[0], centroid[1], centroid[2]))

#----- #4 -----#
points = []
for i in range(2):
    point = tuple(map(int, input().split(' ')))
    if len(point) == 2:
        points.append(Vector.vector2d(point[0], point[1]))
    else:
        points.append(Vector(point[0], point[1], point[2]))
print('Площадь параллелограма:', abs(points[0] @ points[1]))

#----- #5 -----#
points = []
for i in range(3):
    point = tuple(map(int, input().split(' ')))
    if len(point) == 2:
        points.append(Vector.vector2d(point[0], point[1]))
    else:
        points.append(Vector(point[0], point[1], point[2]))
print('Объем параллелепипеда:', points[0] * (points[1] @ points[2]))
