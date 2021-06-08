import os 
#creat empty list
products = []


if os.path.isfile('products.csv'): #check the file is exist or not
	#read csv
	with open('products.csv', 'r', encoding = 'utf-8') as f: #utf-8 is common encode type.
		for line in f:
			if 'products,price' in line:
				continue
			name, price = line.strip().split(',') #remove '\n' and split ','
			products.append([name, price])
			print(products)
else:
	print("Can't not find file")



#enter your products and price
while True:
	name = input('Please enter product name(If want to quit please enter "q"):　')
	if name == 'q':
		break
	price = input('Please enter the price: ')
	products.append([name, price])

#print purchase record
for p in products:
	print(p[0], 'price is ', p[1])

#add new data back to csv
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('products' + ',' + 'price' + '\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
