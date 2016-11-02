class BinarySearch():
    def __init__(self, a, b):
        '''a is the length, b is the step of the list to be created'''
        self.array = range(b, (a * b) + 1, b)
        self.length = len(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def search(self, value):
        count = 0
        first = 0
        last = len(self.array) - 1

        while True:
            if value == self.array[first]:
                return {'index': first, 'count': count}
            elif value == self.array[last]:
                return {'index': last, 'count': count}
            midpoint = (first + last) // 2

            if value == self.array[midpoint]:
                return {'index': midpoint, 'count': count}

            elif value > self.array[midpoint]:
                first = midpoint + 1

            elif value < self.array[midpoint]:
                last = midpoint - 1

            if first >= last:
                break
            count += 1
        return {'index': -1, 'count': count}
