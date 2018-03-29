import random
import time

Barkas = 100
Sobr = 100

print('###Ножевой бой. По мотивам АнтиКиллера.###')
print('Вы выступаете в роли Баркаса, в заключительной схватке с Собровцем.')

time.sleep(1)

print('Инструкции:')
print('Для нанесения свинга в голову, введите "1"')
print('Для нанесения тычка в корпус, введите "2"')

time.sleep(1)
print('-------------------------------------------')
print('-Знаешь ножевой бой. Где служил?')
print('-Тебя там не было.')

while Barkas > 0 and Sobr > 0:
	attack_barkas_head = random.randrange(10, 40)
	attack_sobr_head = random.randrange(20, 50)

	attack_barkas_body = random.randrange(5, 80)
	attack_sobr_body = random.randrange(10, 100)

	block_roll_barkas = random.randrange(1, 100)
	block_roll_sobr = random.randrange(10,100)

	value_attack_sobr = random.randrange(1,2) # какая атака Собра. 

	attack_B = int(input())	# 1 = head, 2 = body

	if attack_B == 1:	# атака в голову
		if block_roll_barkas > block_roll_sobr:
			Sobr = Sobr - attack_barkas_head
			print('Баркас нанес в голову: ', attack_barkas_head)
			print('HP Баркаса: ', Barkas, 'HP Собра: ', Sobr)
			continue
		elif block_roll_barkas < block_roll_sobr:
			print('Собр отразил атаку')
			if value_attack_sobr == 1:
				Barkas = Barkas - attack_sobr_head
				print('Собр нанес в голову: ', attack_sobr_head)
				print('HP Баркаса: ', Barkas, 'HP Собра: ', Sobr)
				continue	
			elif value_attack_sobr == 2:
				Barkas = Barkas - attack_sobr_body
				print('Собр нанес в тело: ', attack_sobr_head)
				print('HP Баркаса: ', Barkas, 'HP Собра: ', Sobr)
				continue
	elif attack_B == 2:	# атака в тело
		if block_roll_barkas > block_roll_sobr:
			Sobr = Sobr - attack_barkas_body
			print('Баркас нанес в тело: ', attack_barkas_body)
			print('HP Баркаса: ', Barkas, 'HP Собра: ', Sobr)
			continue
		elif block_roll_barkas < block_roll_sobr:
			print('Собр отразил атаку')
			if value_attack_sobr == 1:
				Barkas = Barkas - attack_sobr_head
				print('Собр нанес в голову: ', attack_sobr_body)
				print('HP Баркаса: ', Barkas, 'HP Собра: ', Sobr)
				continue
			elif value_attack_sobr == 2:
				Barkas = Barkas - attack_sobr_body
				print('Собр нанес в тело: ', attack_sobr_body)
				print('HP Баркаса: ', Barkas, 'HP Собра: ', Sobr)
				continue
if Barkas < 1:
	print('Жаль, что меня там не было')
		
elif Sobr < 1:			
	print('Баркас остался жив.')
		


			 
 
