g=input('請輸入身高')
w=input('請輸入體重')
g=float(g)
w=float(w)
h=g/100
b=w/(h*h)
b=int(b)
if b<18.5:
    print('你的BMI為',b,'體中過輕')
elif b>=18.5 and b<24:
	print('你的BMI為',b,'體重正常')
elif b>=24 and b<27:
	print('你的BMI為',b,'過重體重')
elif b>=27 and b<30:
	print('你的BMI為',b,'輕度肥胖')
elif b>=30 and b<35:
	print('你的BMI為',b,'中度肥胖')
elif b >= 35: 
	print('你的BMI為',b,'重度肥胖')
