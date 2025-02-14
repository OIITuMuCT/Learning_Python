def fetcher(obj, index):
    try:
        return obj[index]
    except IndexError:
        print(f'got exception max length = {len(obj)}')

if __name__ == "__main__":
    x = "spammer"
    print(fetcher(x, 3))
    print(fetcher(x, 7))
