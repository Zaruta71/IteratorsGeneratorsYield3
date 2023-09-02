class NestedIterator:
    def __init__(self, nested_list):
        self.stack = nested_list[::-1]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            item = self.stack.pop()

            if isinstance(item, list):
                self.stack.extend(item[::-1])
            else:
                return item

        raise StopIteration
