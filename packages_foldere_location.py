#to check the packages of python use the code. Here you can also see the packages install via 'pip'
import site
print(site.getsitepackages())

#for specific package location
import site
import pathlib #give any package name
print(pathlib.__file__)