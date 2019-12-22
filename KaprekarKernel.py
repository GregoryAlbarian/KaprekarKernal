#this function return -1 if it possible_number is not a real number
#this function works!
def input_validation(number):
	if number<1000 or number>9998:
		return False
	first_digit=number%10
	#checking they are not all the same digit
	number = number//10
	while number!=0:
		if first_digit!=number%10:
			return True	#implies all are the same

		number=number//10
	return False

#this function works!
def assign_place_values(digit_list):
	full_number = 0
	digit_list = list(digit_list)
	for i in range(0,len(digit_list)):
		each_digit=int(digit_list[i])
		full_number+=each_digit*10**(len(digit_list)-i-1)
	return full_number

def kaprekar_operation(digits):
	#make it work for the just in case 999< to 0999
	sorted_list = sorted(str(digits))
	backwards_sort = reversed(sorted_list)

	sorted_list = assign_place_values(sorted_list)
	backwards_sort = assign_place_values(backwards_sort)
	
	return (backwards_sort, sorted_list, backwards_sort-sorted_list)

number = input("Give a four digit, positive number in which not all the digits are alike: ")
while True:
	try:
		number=int(number)
		if input_validation(number):
			break;
		else:
			number=input("Try again: make sure the number is four digits, positive, and not all the numbers are the same ")
	except ValueError:
		number=input ("Try again: give an integer: ")
all_numbers = kaprekar_operation(number)
print(all_numbers[0],"-",all_numbers[1],"=",all_numbers[2])

while all_numbers[2]!=6174:
	all_numbers=kaprekar_operation(all_numbers[2])
	print(all_numbers[0],"-",all_numbers[1],"=",all_numbers[2])
print("finished! You have reached 6174, the four-digit Kaprekar Kernal")
