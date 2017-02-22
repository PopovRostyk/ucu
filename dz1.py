import math

class Classroom:
    def __init__(self, audience_number, capacity, equipment):
        self.audience_number = str(audience_number)
        self.capacity = float(capacity)
        self.equipment = equipment

    def is_larger(self, classroom):
        if self.capacity > classroom.capacity:
            return True
        if self.capacity == classroom.capacity:
            return 'Equal'
        else:
            return False

    def equipment_differences(self, classroom):
        lst = [items for items in self.equipment if items not in classroom.equipment]
        return lst

    def __str__(self):
        return 'Classroom {0} has a capacity of {1} persons and has the following equipment: '\
            .format(self.audience_number, self.capacity) + str(', '.join(items for items in self.equipment))


class AcademicBuilding:
    def __init__(self, address, classrooms):
        self.address = address
        self.classrooms = classrooms

    def total_equipment(self):
        lst = []
        lst2 = []
        for items in classrooms:
            for item in items.equipment:
                lst.append(item)
        lst.sort()
        for items in lst:
            if lst.count(items) > 1:
                lst2.append((items, lst.count(items)))
                lst.remove(items)
        lst3 = [items[0] for items in lst2]
        for items in lst:
            if items in lst3:
                lst.remove(items)
        for items in lst:
            lst2.append((items, 1))
        return lst2

    def __str__(self):
        repr_str = self.address + '\n'
        for info in classrooms:
            repr_str = repr_str + str(info) + '\n'
        return repr_str


classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
classroom_007 = Classroom('007', 12, ['TV'])
classroom_008 = Classroom('008', 25, ['PC', 'projector'])
classrooms = [classroom_016, classroom_007, classroom_008]
building = AcademicBuilding('Kozelnytska st. 2a', classrooms)


class Point:
    'Represents a point in two-dimensional geometric coordinates'
    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point. The x and y coordinates can be
        specified. If they are not, the point defaults to the origin.'''
        self.move(x, y)

    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x = x
        self.y = y

    def rotate(self, beta, other_point):
        'Rotate point around other point'
        dx = self.x - other_point.get_xposition()
        dy = self.y - other_point.get_yposition()
        beta = math.radians(beta)
        xpoint3 = dx * math.cos(beta) - dy * math.sin(beta)
        ypoint3 = dy * math.cos(beta) + dx * math.sin(beta)
        xpoint3 = xpoint3 + other_point.get_xposition()
        ypoint3 = ypoint3 + other_point.get_yposition()
        return self.move(xpoint3, ypoint3)

    def get_xposition(self):
        return self.x

    def get_yposition(self):
        return self.y

    def __add__(self, other):
        new_x = self.get_xposition() + other.get_xposition()
        ney_y = self.get_yposition() + other.get_yposition()
        return Point(new_x, ney_y)

    def __iadd__(self, other):
        self.x += other.get_xposition()
        self.y += other.get_yposition()
        return self.x, self.y

    def __sub__(self, other):
        new_x = self.get_xposition() - other.get_xposition()
        new_y = self.get_yposition() - other.get_yposition()
        return Point(new_x, new_y)

    def __isub__(self, other):
        self.x -= other.get_xposition()
        self.y -= other.get_yposition()
        return self.x, self.y

    def __mul__(self, other):
        new_x = self.get_xposition() * other
        new_y = self.get_yposition() * other
        return Point(new_x, new_y)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self.x, self.y

    def __truediv__(self, other):
        new_x = self.get_xposition() / other
        new_y = self.get_yposition() / other
        return Point(new_x, new_y)

    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        return self.x, self.y

    def __floordiv__(self, other):
        new_x = self.get_xposition() // other
        new_y = self.get_yposition() // other
        return Point(new_x, new_y)

    def __ifloordiv__(self, other):
        self.x //= other
        self.y //= other
        return self.x, self.y

    def __str__(self):
        return 'x: {}, y: {}'.format(self.get_xposition(), self.get_yposition())


class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def get_way(self):
        length = (((self.point2.get_xposition() - self.point1.get_xposition())**2) +
                  (self.point2.get_yposition() - self.point1.get_yposition())**2)**(1/2)
        return length


class Triangle:
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.side1 = Line(self.point_1, self.point_2).get_way()
        self.side2 = Line(self.point_1, self.point_3).get_way()
        self.side3 = Line(self.point_2, self.point_3).get_way()

    def is_triangle(self):
        if self.side1 + self.side2 <= self.side3:
            return False
        elif self.side2 + self.side3 <= self.side1:
            return False
        elif self.side1 + self.side3 <= self.side2:
            return False
        else:
            return True

    def display(self):
        print(self.side1, self.side2, self.side3)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        return (self.perimeter()/2 * (self.perimeter()/2 - self.side1) *
                (self.perimeter()/2 - self.side2) * (self.perimeter()/2 - self.side3)) ** (1/2)


class Building:
    def __init__(self, house, address):
        self.house = house
        self.address = address


class House:
    pass

