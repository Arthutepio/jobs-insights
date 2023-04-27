def read():
    with open("arquivo.csv", encoding="utf8") as file:
        data = csv.reader(file, delimiter=",", quotechar='"')
        print(data)

    raise NotImplementedError