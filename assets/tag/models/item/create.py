prefix = input('prefix (eg. map, mode, rating, particle): ')
selection = input('selection?: ')
amount = int(input('how much?: '))

index = 0
while index <= amount:
    if selection == 'n':
        with open(f'{prefix}_{index}.json', 'w') as file:
            file.write(f'''{{
	"parent": "minecraft:item/generated",
	"textures": {{
		"layer0": "tag:item/{prefix}_{index}"
	}},
	"display": {{
		"thirdperson_righthand": {{
			"scale": [0, 0, 0]
		}},
		"thirdperson_lefthand": {{
			"scale": [0, 0, 0]
		}},
		"firstperson_righthand": {{
			"scale": [0, 0, 0]
		}},
		"firstperson_lefthand": {{
			"scale": [0, 0, 0]
		}},
		"ground": {{
			"scale": [0, 0, 0]
		}},
		"head": {{
			"scale": [0, 0, 0]
		}},
		"fixed": {{
			"scale": [1, 1, 1],
			"rotation": [0, -180, 0]
		}}
	}}
}}''')
    else:
        with open(f'sel_{prefix}_{index}.json', 'w') as file:
            file.write(f'''{{
	"parent": "minecraft:item/generated_18",
	"textures": {{
		"layer0": "tag:item/{prefix}_{index}",
        "layer1": "tag:item/sel"
	}},
	"display": {{
		"thirdperson_righthand": {{
			"scale": [0, 0, 0]
		}},
		"thirdperson_lefthand": {{
			"scale": [0, 0, 0]
		}},
		"firstperson_righthand": {{
			"scale": [0, 0, 0]
		}},
		"firstperson_lefthand": {{
			"scale": [0, 0, 0]
		}},
		"ground": {{
			"scale": [0, 0, 0]
		}},
		"head": {{
			"scale": [0, 0, 0]
		}},
		"fixed": {{
			"scale": [1, 1, 1],
			"rotation": [0, -180, 0]
		}}
	}}
}}''')
    index += 1

print ('done')