class Complex():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)
    def __truediv__(self, other):
        x1 = self.x
        x2 = other.x
        y1 = self.y
        y2 = other.y
        return Complex((x1*x2 + y1*y2) / (x2**2 + y2**2), (y1*x2 - x1*y2) / (x2**2 + y2**2))
    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5
    def __repr__(self):
        if self.y > 0:
            return '{} + {}i'.format(self.x, self.y)
        else:
            return '{} {}i'.format(self.x, self.y)
    def __str__(self):
        if self.y > 0:
            return '{} + {}i'.format(self.x, self.y)
        else:
            return '{} {}i'.format(self.x, self.y)
