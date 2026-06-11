def set_to_dict(pets: set[str]) -> dict[str, int]:
    return {pet: index for index, pet in enumerate(pets)}

result = set_to_dict({'dog', 'cat', 'fish'})
