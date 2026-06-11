def even_square_odd_cube() -> list[int]:
    return [i * i if i % 2 == 0 else i * i * i for i in range(1, 21)]

result = even_square_odd_cube()
