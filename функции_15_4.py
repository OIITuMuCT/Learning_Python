numbers = [
    (10, 10, 10),
    (30, 45, 56),
    (81, 39),
    (1, 2, 3),
    (12,),
    (-2, -4, 100),
    (1, 2, 99),
    (89, 9, 34),
    (10, 20, 30, -2),
    (50, 40, 50),
    (34, 78, 65),
    (-5, 90, -1, -5),
    (1, 2, 3, 4, 5, 6),
    (-9, 8, 4),
    (90, 1, -45, -21),
]
lst = [-22, -20, -18, -16, -5, -4, -3, -2, 7, 9]


def avrg(numbers):
    return sum(numbers) / len(numbers)

def main():

    print('min(numbers, key=sum)', min(numbers, key=sum))
    print("max(numbers, key=sum)", max(numbers, key=sum))
    print(min(numbers, key=avrg))
    print(max(numbers, key=avrg))



main()
