#he thuc herong
import math #note:dùng công thức tính toán phải dùng "import math"
print("Nhập số đo ba cạnh của tam giác:")
a = eval(input('Cạnh a ='))
b = eval(input('Cạnh b ='))
c = eval(input('Cạnh c ='))
p = (a+b+c)/2
S= math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác là:",S)
