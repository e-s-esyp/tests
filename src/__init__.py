import numpy as np


# from sklearn import preprocessing

def load1():
    # url with dataset
    file = "/home/gene/Загрузки/data/abalone.data"
    # load the CSV file as a numpy matrix
    global dataset
    dataset = np.loadtxt(file, delimiter=",",
                         dtype={'names': ('gender', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'i'),
                                'formats': ('a1', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'i')})


def load2():
    # url with dataset
    file = "/home/gene/Загрузки/data/1"
    # load the CSV file as a numpy matrix
    dataset = np.loadtxt(file, delimiter=",",
                         dtype={'names': ('gender', 'p1', 'p2'),
                                'formats': ('a10', 'a10', 'a10')})


def test1():
    d = [(1 + i, "f" * (i % 6), 3 + i, 4 + i) * 5 for i in range(100000)]
    x = [i[1:-1] for i in d]
    y = [i[-1:] for i in d]
    print(x)
    print(y)


def test2():
    x = [(1, 2), (3, 4), (5, 6), (7, 8)]
    print(x[1:])

def test3():
    global dataset
    load1()
    # print(dataset)
    x = [(i[1], i[2], i[3]) for i in dataset[0:10]]
    print(x)
    print(dataset[0][0])
    # y = [i[-1] for i in dataset]
    # print(y)
    # normalized_x = preprocessing.normalize(x)
    # print(normalized_x)

if __name__ == "__main__":
    test3()
