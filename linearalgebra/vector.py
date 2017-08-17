from functools import reduce
from math import sqrt, acos, pi
from decimal import Decimal, getcontext
getcontext().prec = 10

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates  = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)  

    def magnitude(self):
        # instructor solution here:
        # coordinates_squared = [x**2 for x in self.coordinates]
        # return sqrt(sum(coordinates_squared))
        squared_coordinates  = [x*x for x in self.coordinates]
        mag = sqrt(reduce((lambda x, y: x + y), squared_coordinates))
        return Decimal(mag)

    def normalized(self):
        try:
            mag = self.magnitude()
            return  self.times_scalar((Decimal(1.0)/mag))
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot_prod(self,w):
        new_coordinates = [x*y for x,y in zip(self.coordinates, w.coordinates)]
        return sum(new_coordinates)

    def angle_btwn(self,w, deg = False):
        try:
            a1 = self.normalized()
            a2 = w.normalized()
            angle = acos(a1.dot_prod(a2))    
            if deg:
                angle =  angle * 180. / pi
            return angle
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute angle with zero vector')
            else:
                raise e

    def isParallel(self,v):
        return (self.is_zero() or v.is_zero() or
          self.angle_btwn(v) == 0 or self.angle_btwn(v) == pi)

    def is_orthogonal_to(self,v,tolerance=1e-10):
        return abs(self.dot_prod(v)) < tolerance

    def is_zero(self,tolerance=1e-10):
        return self.magnitude() < tolerance


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


# a = Vector([-0.221,7.437])
# b = Vector([8.813,-1.331,-6.247])

# c = Vector([5.581,-2.136])
# d = Vector([1.996,3.108, -4.554])

# print (a.magnitude())
# print (b.magnitude())
# print (c.normalized())
# print (d.normalized())

# v = Vector([7.887,4.138])
# w = Vector([-8.802,6.776,])
# print(v.dot_prod(w))

# v = Vector([-5.955,-4.904,-1.874])
# w = Vector([-4.496,-8.755, 7.103])
# print(v.dot_prod(w))

# v = Vector([3.183,-7.627])
# w = Vector([-2.668,5.319])
# print(v.angle_btwn(w))


# v = Vector([7.35,0.221,5.188])
# w = Vector([2.751,8.259,3.985])
# print(v.angle_btwn(w,1))

v = Vector(['-7.579', '-7.88'])
w = Vector(['22.737', '23.64'])
print('Parallel?: ', v.isParallel(w))
print('OrTh?: ', v.is_orthogonal_to(w))

v = Vector(['-2.029','9.97','4.127'])
w = Vector(['-9.231', '-6.639', '-7.245'])
print('Parallel?: ', v.isParallel(w))
print('OrTh?: ', v.is_orthogonal_to(w))

v = Vector(['-2.328', '-7.284', '-1.214'])
w = Vector(['-1.821', '1.072', '-2.94'])
print('Parallel?: ', v.isParallel(w))
print('OrTh?: ', v.is_orthogonal_to(w))




