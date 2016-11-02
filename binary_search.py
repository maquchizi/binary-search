class BinarySearch(list):
    def __init__(self, a, b):
        '''
            a is the length, b is the step/increment of the list to be created
        '''
        super(BinarySearch, self).__init__()
        data = [x for x in range(b, (a * b) + 1, b)]
        self.length = len(data)
        self.extend(data)

    def search(self, value):
        count = 0
        first = 0
        last = len(self) - 1

        while True:
            if value == self[first]:
                return {'index': first, 'count': count}
            elif value == self[last]:
                return {'index': last, 'count': count}
            midpoint = (first + last) / 2

            if value == self[midpoint]:
                return {'index': midpoint, 'count': count}

            elif value > self[midpoint]:
                first = midpoint + 1

            elif value < self[midpoint]:
                last = midpoint - 1

            if first >= last:
                break
            count += 1
        # Return this if no match was found
        return {'index': -1, 'count': count}
