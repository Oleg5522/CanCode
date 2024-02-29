"Concatenation"
operator_code="A987"
part_id = "56p"
item_number = operator_code + part_id
print(item_number)

"2 variables"
first_name = "Oleg"
last_name = "Bez"

full_name = first_name+ " " + last_name
print(full_name)

'''Multiplication'''
greeting = 'hip hop hoor' * 3
print(greeting)

my_fav = 'Purple' * 5
print(my_fav)

#Reference vs Value equality == vs is
x = 'hello'
str2 = 'HeLLo'.lower()
print(x)
print(str2)

test_char = 'b'
test_string = 'bananas'
print(test_char in test_string)

alphabet = 'gfytuvukydtflyiudu'
L_of_A = len(alphabet)
print(L_of_A)

animal = 'crocodile'
L_of_Croco = len(animal)
print(L_of_Croco)

ex_1 = 'cerEal' #capitalize
print(ex_1.capitalize())
print('cereAl'.capitalize())

ex_3 = 'HjYffsRRy'
print(ex_3)

word_4 = 'Good Evening'
print(word_4)
print(word_4.center(100))

ex_4 = 'Hello World'
print(ex_4.center(1))

ex_5 = 'Yikjgxtxjgvkjbkglgilhv'
print(ex_5.count(ex_5))

ex_7 = 'Opklhvftsrecghv'
print(ex_7.find(ex_7))

#test7 = input('What is your favorite actress ?', )
#print(test7)

word_5='HospLitAl'
print(word_5.casefold())
print('SfgTrdG5'.casefold())

word_6='gfhjuiGfrg'
print(word_6.count('g'))

word_7='I\tam\t tab '
print(word_7)
print(word_7.expandtabs(1))
word8='I\nam\nnewline'
print(word8)

word_9='JghdtdrE'
print(word_9.find('d'))

word_10='Hgudhjdtew'
print(word_10.index('H'))

test_1='Abcde'
test_2='012345762'
print(test_1.isalnum())
print(test_2.isalnum())

ex_8='    Jhgfy     '
str=ex_8.strip()
print(str)
print(len(str))
print(len(ex_8))

word_main=input('Input word', )
length_w_m=len(word_main)
print('*'*(length_w_m+2))
print("*"+word_main+'*')
print('*'*(length_w_m+2))

input1 = input('Input yor name')
print(type(input1))
int=int(input1)
print(type(int))

input_num1 = input("Input your number")
result = input_num1.isdigit()
print('Number or not', result)
print(f'If {input_num1} number or not?', result)
