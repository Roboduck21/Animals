import src.classes.Cat as ct
import src.classes.Dog as dg

# name the cats
daisy = ct.Cat()
fern = ct.Cat()
fern.set_name('Fern')
daisy.set_name('Daisy')
# name the dogs
ruby = dg.Dog()
ruby.set_name('Ruby')
emma = dg.Dog()
emma.set_name('Emma')
buster = dg.Dog()
buster.set_name('Buster')
#
# # example one
# print('example one')
# daisy.meow()
# print(daisy.name)
# print(fern.name)
# fern.name = 'Woops'
# print(fern.name)
#
# # example two
# print('example two')
# ruby.bark()
# print('\n', str(fern.meow()))
# fern.meow()
# fern.set_name(fern.meow())
# print(fern.name)

# example three
print('\nexample three')
# NewCat = ct.Cat()
# NewCat.set_name(input("Enter your cat's name: "))
# print(NewCat.name)
DogNames = [ruby.name, emma.name, buster.name]
print(DogNames)
ruby.set_age(10)
emma.set_age(2)
buster.set_age(10)
DogAges = [ruby.age, emma.age, buster.age]
print(DogAges)
