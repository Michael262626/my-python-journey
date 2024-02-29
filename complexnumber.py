class Complex:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    # def __add__(self, other):
    #     return self.left + other.left and self.right + other.right

    def __add__(self, other):
        return Complex(self.left + other.left, self.right + other.right)

    def __sub__(self, other):
        return Complex(self.left - other.left, self.right - other.right)

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right

    def __gt__(self, other):
        return self.left + self.right > self.right + self.left

    def __lt__(self, other):
        return self.left + self.right < self.right + self.left

    def __repr__(self):
        return f"{self.left}j {"+" if self.right > 0 else "-"} {abs(self.right)}i"


c1 = Complex(2, 3)
c2 = Complex(5, -2)
c3 = Complex(2, 3)
print(c1)
print(c2)
print(c1 + c2)
print(c1 - c2)
print(c1 == c3)
print(c1 > c2)
print(c1 < c2)