# slicing = create a substring by extracting elements from another string
# indexing[] or slice ()
# [start:stop:step]

name = "Farhan Code"
badge = "Gojo Satoru"

first_name = name[0:6]
last_name = name[7:11]
reversed_name = badge[::-1]


print(first_name +" "+ last_name)
print(reversed_name)

# SLICING FUNCTION TUTORIAL
#jika string dihitung dari kiri maka (+) index jika dari kanan maka (-) index

website1 = "http://google.com"
website2 = "http://xnxx.com"

slice = slice(7,-4)
print(website1[slice])
print(website2[slice])