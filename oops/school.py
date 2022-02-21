class Line:
    def __init__(self,cord1,cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def distance(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2

        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    def slope(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2

        return (y2-y1)/(x2-x1)

