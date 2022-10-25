def flatten(nested_list):
    flat_list = []
    for element in nested_list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list
