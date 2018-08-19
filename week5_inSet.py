
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals
        
    def intersect(self, other):
        intersect = []
        intersect = [element for element in self.vals if other.member(element)]
        intersect_int = intSet()
        for element in intersect:
            intersect_int.insert(element)
        return intersect_int
        
    def __len__(self):
        return len(self.vals)
    
    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'


setA = intSet()
setB = intSet()
setA.insert(1)
setA.insert(2)
setA.insert(3)
setA.insert(4)
setA.insert(5)
setB.insert(3)
setB.insert(4)
setB.insert(5)
setB.insert(6)
setB.insert(7)
print(setA.intersect(setB))

print(setB.len())

print(intSet.len(setA))

