def fetcher(obj, index):
    if int(index) >= len(obj):
        return "Index Error"
    else:
        return obj[index]
    
if __name__ =='__main__':
    x = 'spam'
    print(fetcher(x, 3))
    