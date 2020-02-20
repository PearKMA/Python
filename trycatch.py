try:
    x = 8
    y = 0
    z = x/y
except:
    print('Lỗi kìa!')

try:
    pass
except NameError:
    pass
except ZeroDivisionError as e:
    pass