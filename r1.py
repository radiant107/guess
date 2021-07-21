import random
r = random.randint(1, 100) # 讓程式隨機選一個數字
count = 0
while True:
	r1 = input('猜猜看1-100間的任一整數: ')
	r1 = int(r1)
	count += 1   # count = count + 1 的簡寫法
	if r1 == r:
		print('恭喜猜對了！')
		break
	elif r1 > r:
		print('猜錯了，數字太大')
	elif r1 < r: 
		print('猜錯了，數字太小')
print('你總共猜了', count,'次')
