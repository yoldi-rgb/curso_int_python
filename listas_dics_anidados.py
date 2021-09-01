def run():
    my_list = [1,"Hello", True,3.5]
    my_dict = {"firstname": "yoldi", "lastname":"Carrada"}

    super_list = [
        {"firstname": "yoldi", "lastname":"Carrada"},
        {"firstname": "Eliza", "lastname":"Gonzales"},
        {"firstname": "Emika", "lastname":"Carranza"},
        {"firstname": "Aline", "lastname":"Flamego"},

    ]

    super_dict = {
        "natural_nuns": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.345]
    }

    for key , value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i)


if __name__ == '__main__':
    run()
