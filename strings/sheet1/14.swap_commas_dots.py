def swap_commas_dots(s):
    return s.replace(",", "<tmp>").replace(".", ",").replace("<tmp>", ".")

result = swap_commas_dots("23,45.89,78.90")  # "23.45,89.78,90"
