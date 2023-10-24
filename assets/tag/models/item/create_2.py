prefix = input('prefix: ')
amount = int(input('how much?: '))

index = 0
while index <= amount:
	with open(f'{prefix}_{index}.json', 'w') as file:
		file.write(f'''{{
	"parent": "tag:item/{prefix}",
	"textures": {{
		"{prefix}": "tag:block/{prefix}_{index}"
	}}
}}''')
	index += 1

print ('done')