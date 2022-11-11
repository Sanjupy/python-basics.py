#index operator []=gives access to sequence of elements(Str,lists,tuples)

from distutils.command.build_scripts import first_line_re


name="sanjeevKUmar"

if(name[0].islower()):
    name=name.capitalize()

first_name=name[0:7].upper()
last_name=name[7:12].lower()
print(name)


print(first_name)
print(last_name)