#str.format() =optional method that gives users
  #              more control when displaying output

from cgitb import text


animal="cow"
item="moon"

print("the"+animal+"jumped over the"+item)

print("the {} jumped over the {}".format("cow","moon"))

print("the {} jumped over the {}".format(animal,item))

print("the {} jumped over the {}".format(item,animal))

print("the {1} jumped over the {0}".format(animal,item)) #positional arguent

print("the {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument

print("the {animal} jumped over the {animal}".format(animal="cow",item="moon"))

text="the {} jumped over {}"
print(text.format(animal,item))

