name = input("Comment tu t'appele?")
while name != "":
	for x in range(100):
		print(name, end = " ")
	print()
	name = input("Ecriez autre nom, ou simplement [Entrez] pour quitte: ")
print("Merci beacoup pour le game!")