import re
p = re.compile('[a-z]+', re.IGNORECASE)  # or re.compile('UF*')

print(p.match("this is my string"))
print(p.match("this"))
print(p.match(" "))
print(p.match("thisismystring"))
print(p.match('123'))

