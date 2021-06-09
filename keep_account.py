import os 

#read file
def read_file(filename):
	products = [] #creat empty list
	with open(filename, 'r', encoding = 'utf-8') as f: #utf-8 is common encode type.
		for line in f:
			if 'products,price' in line:
				continue
			name, price = line.strip().split(',') #remove '\n' and split ','
			products.append([name, price])
	return products

#enter your products and price
def usr_input(products):
	while True:
		name = input('Please enter product name(If want to quit please enter "q"):　')
		if name == 'q':
			break
		price = input('Please enter the price: ')
		products.append([name, price])
	return products

#print purchase record
def print_purchase(products):
	for p in products:
		print(p[0], 'price is ', p[1])

#add new data back to csv
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('products' + ',' + 'price' + '\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


def main(filename):
	if os.path.isfile(filename): #check the file is exist or not
		products = read_file(filename)					
	else:
		print("Can't not find file")
	products = usr_input(products)
	print_purchase(products)
	write_file(filename, products)

filename = 'products.csv'	
main('products.csv')

