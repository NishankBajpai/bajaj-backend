def split_data(data):
    numbers = [item for item in data if isinstance(item, int) or item.isdigit()]
    alphabets = [item for item in data if isinstance(item, str) and item.isalpha()]
    highest_lowercase = max([item for item in alphabets if item.islower()], default="", key=str.lower)
    return numbers, alphabets, highest_lowercase
