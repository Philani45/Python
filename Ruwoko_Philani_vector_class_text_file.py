class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other_vector):
        if isinstance(other_vector, Vector):
            new_x = self.x + other_vector.x
            new_y = self.y + other_vector.y
            new_z = self.z + other_vector.z
            return Vector(new_x, new_y, new_z)
        else:
            raise TypeError("Unsupported operand type. Vector expected.")

# Example:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

result = v1 + v2
print("Result of vector addition:", result.x, result.y, result.z)
