def one(a):
    print("Da da da")

def two(a):
    print("Ne ne ne")

data = {
    "a": one,
    "b": two,
}

def fabric():
    val = input("pipa: ")

    data[val]("a")