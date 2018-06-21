import datetime
food = raw_input("whats the best food?")
drink = raw_input("whats the best drink?")

print food + " " + drink

if food == "lasagne" and drink == "coke":
	sauce = raw_input("whats the best sauce?")

first_name = raw_input("First name:")
second_name = raw_input("Second name:")

print first_name + " " + second_name

if first_name == "rory" and second_name == "loughran":
	access_code = raw_input("Provide access code:")
	print access_code
	
if access_code == "230103" or "240103":
	print "Access granted"
else:
	print "Access denied"

x = datetime.datetime.now()

print(x.strftime("%a"))
