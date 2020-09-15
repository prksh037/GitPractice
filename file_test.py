import re

with open('test.txt') as f:
    data = f.read()

#print('Contents of the file test.txt: ', data)
#print('4th line in test.txt: ', data[3])


emailRegex = re.compile(r'\d{10}')
mo = re.findall(emailRegex,data)
print(mo)
