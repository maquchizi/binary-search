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
                return {'count': count, 'index': first}
            elif value == self[last]:
                return {'count': count, 'index': last}

            midpoint = (first + last) // 2

            if value == self[midpoint]:
                return {'count': count, 'index': midpoint}
            elif value > self[midpoint]:
                first = midpoint + 1
            else:
                last = midpoint - 1

            if first >= last:
                break

            count += 1
        # Return this if no match was found
        return {'count': count, 'index': -1}
