class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._array = self._make_array(self._capacity)
    
    def _make_array(self, capacity):
        return [0] * capacity

    def _resize(self, new_capacity):
        print(f"Resizing from capacity {self._capacity} to {new_capacity}")
        new_array = self._make_array(new_capacity)
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def append(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = value
        self._size += 1
        print(f"Appended {value}, size = {self._size}, capacity = {self._capacity}")

    def get(self, index):
        if 0 <= index < self._size:
            return self._array[index]
        raise IndexError("Index out of bounds")

    def set(self, index, value):
        if 0 <= index < self._size:
            self._array[index] = value
        else:
            raise IndexError("Index out of bounds")

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity


if __name__ == "__main__":
    da = DynamicArray()
    for i in range(10):
        da.append(i)

    print("\nAccessing element at index 5:")
    print("Element:", da.get(5))

    print("\nUpdating element at index 5 to 99")
    da.set(5, 99)
    print("Updated element:", da.get(5))

    print(f"\nFinal size: {da.size()}, capacity: {da.capacity()}")
