# coding:shift-jis

while True:
	height=input('�g��(m)?:')
	if len(height)==0:
		break
	height=float(height)
	weight=float(input('�̏d(kg)?:'))
	bmi=weight/pow(height,2)
	
	print('BMI��%0.1f�ł��B' %bmi)
	if bmi<18.5:
		print('�����₹�����ł��B')
	elif 18.5<=bmi<25.0:
		print('�W���I�ȑ̌^�ł��B')
	elif 25.0<=bmi<30.0:
		print('���������Ă��܂��B')
	else:
		print('���x�̔얞�ł�')
		