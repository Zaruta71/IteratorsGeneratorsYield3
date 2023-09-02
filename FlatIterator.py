nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator:
    def __init__(self, nested_list):
        self.stack = nested_list[::-1]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        item = self.stack.pop()

        if isinstance(item, list):
            self.stack.extend(item[::-1])

            return next(self)

        return item


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

