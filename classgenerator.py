# This is a C++ class generator

def classGenerating():
	# atributes is an array
	className = input('Name of class: ')
	
	print("Now type your atributes, type 9 to stop")
	atributes_list = []
	mayuscula_list = []
	atribute_type = []
	while True:
		enter_atribute = input("atribute: ")
		if enter_atribute == '9':
			break
		else:
			atributes_list.append(enter_atribute)
			atribute_type.append(input("type:"))
			s = list(enter_atribute)
			s[0] = s[0].upper()
			mayuscula_list.append("".join(s)) 

	print(atributes_list)
	print(atribute_type)


	with open('newClass.txt', 'w') as f:
		f.write('%s{' % (className))
		
		f.write('\npublic:')
		f.write('\n%s();' % (className))
		f.write('\n%s(' % (className))
		for i in range(len(atribute_type)):
			f.write(' %s,'%(atribute_type[i]))
		f.write(');')	

		f.write('\n~%s();' % (className))

		counter = 0
		for i in range(len(atributes_list)):
			getter = '\n%s get%s();' % (atribute_type[counter], mayuscula_list[i])
			f.write(getter)
			counter += 1

		counter_2 = 0
		for i in range(len(atributes_list)):
			f.write('\nvoid set%s(%s);'%(mayuscula_list[i], atribute_type[counter_2]))
			counter_2 += 1

		f.write('\nprivate:')
		counter_3 = 0
		for i in range(len(atributes_list)):
			f.write('\n%s %s;' % (atribute_type[counter_3], atributes_list[i]))
			counter_3 +=1

		f.write('\n};')

		f.write('\n%s::%s(){}' % (className, className))
		f.write('\n%s::%s(' % (className, className))
		for i in range(len(atribute_type)):
			f.write(' %s,'%(atribute_type[i]))
		f.write('){')
		for i in range(len(atributes_list)):
			f.write('\n   %s=;' % (atributes_list[i]))
		f.write('\n}')
		f.write('\n%s::~%s();' % (className, className))

		# Getters
		for i in range(len(atributes_list)):
			f.write('\n%s %s::get%s(){'%(atribute_type[i], className, mayuscula_list[i]))
			f.write('\n   return %s;'%(atributes_list[i]))
			f.write('\n}')
		# Setters
		for i in range(len(atributes_list)):
			f.write('\nvoid %s::set%s(%s){'%(className, mayuscula_list[i], atribute_type[i]))
			f.write('\n   %s=;'%(atributes_list[i]))
			f.write('\n}')



classGenerating()