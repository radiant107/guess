import random # 載入random module
start = input('請決定隨機數字範圍開始值： ')
end = input('請決定隨機數字範圍結束值： ')
r = random.randint(int(start), int(end)) # 讓程式隨機選一個數字 # 用int將字串轉成數字
count = 0
while True:
	r1 = input('猜猜看區間內的任一整數: ')
	r1 = int(r1)
	count += 1   # count = count + 1 的簡寫法
	if r1 == r:
		print('恭喜猜對！')
		break
	elif r1 > r:
		print('猜錯了，數字太大')
	elif r1 < r: 
		print('猜錯了，數字太小')
print('你總共猜了', count,'次')
