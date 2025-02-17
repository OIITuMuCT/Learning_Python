def test(data):
    return data + 5

test(5)
assert True, test(5)
print(test(5))
# if __debug__:
#     if not test:
#         raise AssertionError(data)