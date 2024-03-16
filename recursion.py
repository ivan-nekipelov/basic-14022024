def summa(_list, i):
    if i == len(_list) - 1:
        return _list[i]
    else:
        return _list[i] + summa(_list, i + 1)


if __name__ == "__main__":
    list_one = [2, 6, 9]
    print(summa(list_one, 0))
