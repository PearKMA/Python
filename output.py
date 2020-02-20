print('In bình thường 15 dấu *\n')
print('*'*15)
#
print('In theo kiểu format: \n')
print('a{0}b{1}c{2}'.format('x','y','z'))
print('\nCăn phải\n')
print('-'*15)
print('{0:>2} {1:>11}'.format('STT','Giá trị'))
print('-'*15)
print('{0:>2} {1:>11}'.format('1',10**10))
print('{0:>2}'.format(1))
print('{0:>11}'.format(10**10))
"""
Kết quả dạng:

---------------
STT     Giá trị
---------------
 1 10000000000

Giải thích:
đầu tiên sẽ nhập 1 vào vị trí 0 sẽ có dạng
---------------
STT     Giá trị
---------------
 1         1 có số ký tự nhỏ hơn 2 -> thêm khoảng trắng trước 1


Tiếp đó chèn thêm 10**10 vào
Chuỗi có dạng 1 1000000000
---------------
STT     Giá trị
---------------
 1 10000000000   chuỗi "1000000000" có số ký tự = 11 nên ko cần thêm
                 ví dụ nếu là "1000" thì sẽ thêm chuỗi " 1 " trước xong thêm khoảng trắng
                 + chuỗi "1000" sao cho đủ 11 ký tự vào sau

"""