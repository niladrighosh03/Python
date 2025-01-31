import converter #use 'import' to import the converter module

from converter import kg_to_lbs #another way to use a specific module or class in a file

wt=converter.kg_to_lbs(70)
print(wt)
print(converter.lbs_to_kg(240))

wt1=kg_to_lbs(50) #we can so directly call the dunction in our program
print(wt1)