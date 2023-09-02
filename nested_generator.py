def nested_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from nested_generator(item)
        else:
            yield item
