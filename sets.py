#Set dalam Python adalah koleksi elemen yang bersifat unik dan tidak berurutan.
# Berbeda dengan dengan tipe data lain seperti list atau tuple,
# set tidak mengizinkan adanya duplikasi elemen. Artinya,
# setiap elemen di dalam Python set pasti bersifat unik.

utensils = {"fork","spoons","knife","bowl"}
dishes = {"bowl","plate","cup","knife"}

print(utensils.difference(dishes))
print(utensils.intersection(dishes))
#utensils.add("plate")
#utensils.remove("plate")
#utensils.update(dishes)

dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)