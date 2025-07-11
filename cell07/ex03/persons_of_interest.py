def famous_births(figures):
    sorted_figures = sorted(figures.values(), key=lambda x: int(x["date_of_birth"]))
    for figure in sorted_figures:
        print(f'{figure["name"]} is a great scientist born in {figure["date_of_birth"]}.')

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)