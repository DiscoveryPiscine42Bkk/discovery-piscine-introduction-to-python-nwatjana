def array_of_names(name_dict):
    full_names = [first.capitalize() + " " + last.capitalize() for first, last in name_dict.items()]
    return full_names
persons ={
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))