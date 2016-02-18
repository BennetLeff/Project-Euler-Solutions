#################################################################
## https://en.wikipedia.org/wiki/Barycentric_coordinate_system ##
## #Conversion_between_barycentric_and_Cartesian_coordinates   ##
## x = a * x1 + b * x2 + c * x3                               ##
## y = a * y1 + b * y2 + c * y3                                ##
## a + b + c = 1                                               ##
## p lies in T if and only if 0 <= a, b, c <= 1                ##
#################################################################

file = open("triangles.txt")
triangles = []
count = 0

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def check_coords(self, px, py):
        self.area = 1.0/2*(-self.y2*self.x3 + self.y1*(-self.x2 + self.x3) + self.x1*(self.y2 - self.y3) + self.x2*self.y3);

        self.s = 1.0/(2*self.area)*(self.y1*self.x3 - self.x1*self.y3 + (self.y3 - self.y1)*px + (self.x1 - self.x3)*py);

        self.t = 1.0/(2*self.area)*(self.x1*self.y2 - self.y1*self.x2 + (self.y1 - self.y2)*px + (self.x2 - self.x1)*py);

        if (1 - self.s - self.t > 0 and self.s > 0 and self.t > 0):
            return True

        else:
            return False

for x in file:
    triangles += [Triangle(int(x.split(",")[0]), int(x.split(",")[1]), int(x.split(",")[2]),
                  int(x.split(",")[3]), int(x.split(",")[4]), int(x.split(",")[5]))]

for tri in triangles:
    if tri.check_coords(0, 0):
        count += 1

print count