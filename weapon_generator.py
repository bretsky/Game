import random 
from numpy.random import choice
from decimal import *

getcontext().prec = 64

def random_weapon(weapon_type='rand', maxlevel=100):

	def rationalize(weight_list):
		weight_sum = 0
		weight_ratio_list = []
		for x in weight_list:
			weight_sum += Decimal(x)
		for x in weight_list:
			x = Decimal(x)
			weight_ratio_list.append(Decimal(Decimal(x)/weight_sum))
		return weight_ratio_list

	def weapon_chooser(weapon_class):
		if weapon_class == 'melee':
			wooden_melee_weapons = ['long staff', 'club', 'nunchaku', 'bokken', 'short staff', 'cane']
			melee_weapons_file = open('melee_weapons.txt')
			melee_weapons = melee_weapons_file.read().splitlines()
			special_melee_weapons_file = open('special_melee_weapons.txt')
			special_melee_weapons = special_melee_weapons_file.read().splitlines()
			melee_rarity_file = open('melee_weapon_rarity.txt')
			melee_rarity_inverse = melee_rarity_file.read().splitlines()
			melee_rarity = []
			for x in melee_rarity_inverse:
				x = int(x)
				melee_rarity.append(Decimal(10**(1/2)) - Decimal(x**(1/2)))
			melee_rarity = rationalize(melee_rarity)
			special_melee_rarity_file = open('special_melee_weapon_rarity.txt')
			special_melee_rarity_inverse = special_melee_rarity_file.read().splitlines()
			special_melee_rarity = []
			for x in special_melee_rarity_inverse:
				x = int(x)
				special_melee_rarity.append(Decimal(10**(1/2)) - Decimal(x**(1/2)))
			special_melee_rarity = rationalize(special_melee_rarity)
			length = len(melee_weapons) + len(special_melee_weapons)
			random_pick = random.randrange(0, length)
			if random_pick < len(melee_weapons):
				random_weapon = choice(melee_weapons, p=melee_rarity)
				if random_weapon in wooden_melee_weapons:
					material = random_material('wood')
				else:
					material = random_material('metal')
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'melee' 
				weapon_attributes['material'] = material[0]
				weapon_attributes['material_stat'] = material[1]
				weapon_attributes['class'] = 'melee'
				weapon_index = melee_weapons.index(random_weapon)
				weapon_rarity = int(melee_rarity_inverse[weapon_index])
				weapon_level = round((int(weapon_rarity*material[1]))**(0.562151993))
				if weapon_level > maxlevel:
					weapon_attributes = weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_name = (material + ' ' + weapon + ' (' + weapon_type + ' - Material Bonus x' + str(weapon_attributes['material_stat']) + ' - Requires Level ' + str(weapon_level) + ' Undetermined Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
			else:
				weapon_attributes = {}
				random_weapon = choice(special_melee_weapons, p=special_melee_rarity)
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'special melee' 
				weapon_attributes['material'] = 'special'
				weapon_attributes['material_stat'] = 1
				weapon_attributes['class'] = 'melee'
				weapon_level = round(int(special_melee_rarity_inverse[special_melee_weapons.index(random_weapon)])**2.09590327429)
				if weapon_level > maxlevel:
					weapon_attributes = weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_name = (weapon + ' (' + weapon_type + ' - No Material Bonus' + ' - Requires Level ' + str(weapon_level) + ' Undetermined Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
		if weapon_class == 'ranged':
			wooden_ranged_weapons = ['shortbow', 'longbow', 'bow', 'blowdart', 'compound bow', 'crossbow', 'baseball bat', 'boomerang']
			ranged_weapons_file = open('ranged_weapons.txt')
			ranged_weapons = ranged_weapons_file.read().splitlines()
			special_ranged_weapons_file = open('special_ranged_weapons.txt')
			special_ranged_weapons = special_ranged_weapons_file.read().splitlines()
			ranged_rarity_file = open('ranged_weapon_rarity.txt')
			ranged_rarity_inverse = ranged_rarity_file.read().splitlines()
			ranged_rarity = []
			for x in ranged_rarity_inverse:
				x = int(x)
				ranged_rarity.append(Decimal(10**(1/2)) - Decimal(x**(1/2)))
			ranged_rarity = rationalize(ranged_rarity)
			special_ranged_rarity_file = open('special_ranged_weapon_rarity.txt')
			special_ranged_rarity_inverse = special_ranged_rarity_file.read().splitlines()
			special_ranged_rarity = []
			for x in special_ranged_rarity_inverse:
				x = int(x)
				special_ranged_rarity.append(Decimal(10**(1/2)) - Decimal(x**(1/2)))
			special_ranged_rarity = rationalize(special_ranged_rarity)
			length = len(ranged_weapons) + len(special_ranged_weapons)
			random_pick = random.randrange(0, length)
			if random_pick < len(ranged_weapons):
				random_weapon = choice(ranged_weapons, p=ranged_rarity)
				if random_weapon in wooden_ranged_weapons:
					material = random_material('wood')
				else:
					material = random_material('metal')
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'ranged' 
				weapon_attributes['material'] = material[0]
				weapon_attributes['material_stat'] = material[1]
				weapon_attributes['class'] = 'ranged'
				weapon_index = ranged_weapons.index(random_weapon)
				weapon_rarity = int(ranged_rarity_inverse[weapon_index])
				weapon_level = round((int(weapon_rarity*material[1]))**(0.562151993))
				if weapon_level > maxlevel:
					weapon_attributes = weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_name = (material + ' ' + weapon + ' (' + weapon_type + ' - Material Bonus x' + str(weapon_attributes['material_stat']) + ' - Requires Level ' + str(weapon_level) + ' Undetermined Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
			else:
				weapon_attributes = {}
				random_weapon = choice(special_ranged_weapons, p=special_ranged_rarity)
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'special ranged' 
				weapon_attributes['material'] = 'special'
				weapon_attributes['material_stat'] = 1
				weapon_attributes['class'] = 'ranged'
				weapon_level = round(int(special_ranged_rarity_inverse[special_ranged_weapons.index(random_weapon)])**2.09590327429)
				if weapon_level > maxlevel:
					weapon_attributes = weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_name = (weapon + ' (' + weapon_type + ' - No Material Bonus' + ' - Requires Level ' + str(weapon_level) + ' Undetermined Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes
		if weapon_class == 'magic':	
			magic_weapons_file = open('magic_weapons.txt')
			magic_weapons = magic_weapons_file.read().splitlines()
			special_magic_weapons_file = open('special_magic_weapons.txt')
			special_magic_weapons = special_magic_weapons_file.read().splitlines()
			magic_rarity_file = open('magic_weapon_rarity.txt')
			magic_rarity_inverse = magic_rarity_file.read().splitlines()
			magic_rarity = []
			for x in magic_rarity_inverse:
				x = int(x)
				magic_rarity.append(Decimal(10**(1/2)) - Decimal(x**(1/2)))		
			magic_rarity = rationalize(magic_rarity)
			special_magic_rarity_file = open('special_magic_weapon_rarity.txt')
			special_magic_rarity_inverse = special_magic_rarity_file.read().splitlines()
			special_magic_rarity = []
			for x in special_magic_rarity_inverse:
				x = int(x)
				special_magic_rarity.append(Decimal(10**(1/2)) - Decimal(x**(1/2)))
			special_magic_rarity = rationalize(special_magic_rarity)
			length = len(magic_weapons) + len(special_magic_weapons)
			random_pick = random.randrange(0, length)
			if random_pick < len(magic_weapons):			
				random_weapon = choice(magic_weapons, p=magic_rarity)
				material = random_material('wood')
				weapon_attributes = {}
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'magic' 
				weapon_attributes['material'] = material[0]
				weapon_attributes['material_stat'] = material[1]
				weapon_attributes['class'] = 'magic'
				weapon_index = magic_weapons.index(random_weapon)
				weapon_rarity = int(magic_rarity_inverse[weapon_index])
				weapon_level = round((int(weapon_rarity*material[1]))**(0.562151993))
				if weapon_level > maxlevel:
					weapon_attributes = weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_name = (material + ' ' + weapon + ' (' + weapon_type + ' - Material Bonus x' + str(weapon_attributes['material_stat']) + ' - Requires Level ' + str(weapon_level) + ' Undetermined Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes				
			else:		
				weapon_attributes = {}
				random_weapon = choice(special_magic_weapons, p=special_magic_rarity)
				weapon_attributes['weapon'] = random_weapon
				weapon_attributes['type'] = 'special magic' 
				weapon_attributes['material'] = 'special'
				weapon_attributes['material_stat'] = 1
				weapon_attributes['class'] = 'magic'
				weapon_level = round(int(special_magic_rarity_inverse[special_magic_weapons.index(random_weapon)])**2.09590327429)
				if weapon_level > maxlevel:
					weapon_attributes = weapon_chooser(weapon_class)
				weapon_attributes['level'] = weapon_level
				material = weapon_attributes['material']
				material = ' '.join(word[0].upper() + word[1:] for word in material.split())
				weapon = weapon_attributes['weapon']
				weapon = ' '.join(word[0].upper() + word[1:] for word in weapon.split())
				weapon_type = weapon_attributes['type']
				weapon_type = ' '.join(word[0].upper() + word[1:] for word in weapon_type.split())
				weapon_name = (weapon + ' (' + weapon_type + ' - No Material Bonus' + ' - Requires Level ' + str(weapon_level) + ' Undetermined Skill' + ')')
				weapon_attributes['name'] = weapon_name
				return weapon_attributes

	def random_material(material_type):
		material_rarity = []
		for x in range(34):
			material_rarity.append(Decimal(34**(1/2)) - Decimal(x**(1/2)))
		material_rarity = rationalize(material_rarity)
		material_dict = materials['dict']
		possible_material_dict = material_dict[material_type]
		possible_material_list = materials[material_type]
		material = choice(possible_material_list, p=material_rarity)	
		material_stat = possible_material_dict[material]
		material_attributes = [material, material_stat]
		return material_attributes

	def weapon_class_chooser():
		classes = ['magic', 'melee', 'ranged']
		weapon_class = random.choice(classes)
		return weapon_class

	if weapon_type == 'rand':
		return weapon_chooser(weapon_class_chooser())
	else:	
		return weapon_chooser(weapon_type)

def weapon_generator(weapons_limit):
	counter = 0
	weapon_list = []
	while counter <= weapons_limit - 1:
		random_weapon_attributes = random_weapon('rand')
		if random_weapon_attributes['class'] == 'melee':
			if random_weapon_attributes['type'] == 'melee':
				weapon_list.append(random_weapon_attributes['name'])
			elif random_weapon_attributes['type'] == 'special melee':
				weapon_list.append(random_weapon_attributes['name'])
			counter += 1
		if random_weapon_attributes['class'] == 'ranged':
			if random_weapon_attributes['type'] == 'ranged':
				weapon_list.append(random_weapon_attributes['name'])
			elif random_weapon_attributes['type'] == 'special ranged':
				weapon_list.append(random_weapon_attributes['name'])
			counter += 1
		if random_weapon_attributes['class'] == 'magic':
			if random_weapon_attributes['type'] == 'magic':
				weapon_list.append(random_weapon_attributes['name'])
			elif random_weapon_attributes['type'] == 'special magic':
				weapon_list.append(random_weapon_attributes['name'])
			counter += 1
	return weapon_list

def user_process(user_input):
	end_process = False
	while end_process != True:
		if user_input != 'end':
			weapon_generator_list = weapon_generator(int(user_input))
			print('')
			for x in range(len(weapon_generator_list)):
				print(weapon_generator_list[x] + '\n')
			return user_process(input('How many more weapons to generate? (Type "end" to close program.) '))
		elif user_input == 'end':
			return 'Closing...'
			sleep(100)
			break

		else:
			return user_process(input('How many more weapons to generate? (Must be a number.) '))

def material_lister():
	metallic_material_file = open('metallic_materials.txt')
	metallic_materials = metallic_material_file.read().splitlines()
	metallic_material_stats = {}
	wooden_material_file = open('wooden_materials.txt')
	wooden_materials = wooden_material_file.read().splitlines()
	wooden_material_stats = {}
	for x in range(len(metallic_materials)):
		metallic_material_stats[metallic_materials[x]] = round((x+1)**1.7)
	for x in range(len(wooden_materials)):
		wooden_material_stats[wooden_materials[x]] = round((x+1)**1.7)
	material_dict = {'metal' : metallic_material_stats, 'wood' : wooden_material_stats}
	dict_list = {'metal' : metallic_materials, 'wood' : wooden_materials, 'dict' : material_dict}
	return dict_list	

materials = material_lister()

print(user_process(input('How many weapons to generate? (Type "end" to close program.) '))
)



