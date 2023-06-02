import json
#Author: Zaheer Khan
#Description: A simple example demonstrating how to process JSON objects using python

print ('JSON Example')

json_string = '{"first_name": "Zaheer", "last_name":"Khan", "module":"Web programming"}'
parsed_json = json.loads(json_string)	#json.loads to convert a string (json) to key:value dictionary
										#works with string and converts it to kind a dictionary
print(parsed_json['first_name'], ' teaches ', parsed_json['module'] ) #access indvidual json elements

#another example
data = {
    'first_name': 'Zaheer',
    'second_name': 'Khan',
    'titles': ['Teacher', 'Developer', 'Researcher']
}


print(json.dumps(data))	#json.dumps coverts python dictionary (json) into string
parsed_json_dump = json.dumps(data)	#json.dumps coverts python dictionary (json) into string
parsed_json = json.loads(parsed_json_dump) 
print(parsed_json['titles'])
# Check more details about json module - https://docs.python.org/3/library/json.html 
