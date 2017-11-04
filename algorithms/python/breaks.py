def squared(arg):
    try:
        sq = int(arg)
        return sq ** 2
    except ValueError:
        return arg * len(arg)

if __name__ == '__main__':
    print(squared(5))
    print(squared("2"))
    print(squared("tim"))
