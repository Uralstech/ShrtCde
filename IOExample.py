from ShrtCde.IO import *

# Feel free to mess around with the function values!

path = input("Enter file path (write): ")
data = input("Enter data to write: ")
encoding = input("Enter encoding of data: (default: utf-8)")
encoding = encoding if encoding != "" else "utf8"

split = " "
data = list(data.split(sep=split))

append = input("Append data? y/n: ")
if append == 'y': readf(path, data, 'a', encoding)
else: readf(path, data, 'w', encoding)

print('\n\n')

path = input("Enter file path (read): ")
encoding = input("Enter encoding of data: (default: utf-8)")
encoding = encoding if encoding != "" else "utf8"

if not findf(path):
    print("File was not found. Exiting program...")
    input()
    quit()

mode = input("Enter read mode:\n-r to read whole file as string\n-rl to read first line as string\n-rls ro read whole file as list\n: ")
data = readf(path, mode, encoding)
print(data, f"\n\n TYPE: {str(type(data))}")
input()