# class E(Exception):
#     def __repr__(self):
#         return 'Not called!'

# raise E('Spam')

class E(Exception):
    def __str__(self):
        return 'Called!'

raise E('spam')