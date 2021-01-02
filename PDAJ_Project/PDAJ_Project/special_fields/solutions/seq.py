import math
import tracemalloc

def generate_koords(n,m):
    koords = []
    for i in range(0,n):
        for j in range(0,m):
            koords.append((i,j))
    return koords

def generate_special_fields_koords(special_fields):
    special_fields_list = []
    for special_field in special_fields:
        koords = []
        special_field = special_field.split(",")
        for i in special_field:
            koords.append(int(i))
        special_fields_list.append(tuple(koords))
    return special_fields_list

def generate_special_fields_number(special_fields):
    spec_field_numbers = {}
    i = 0
    for special_field in special_fields:
        spec_field_numbers[special_field] = i
        i = i + 1
    return spec_field_numbers

def generate_distance(spec_field_numbers,koords):
    results = []
    for koord in koords:
        distances_for_koord = {}
        for key,value in spec_field_numbers.items():
            distance = math.sqrt(math.pow((koord[0]-int(key[0])),2)+(math.pow((koord[1]-int(key[1])),2)))
            distances_for_koord[key] = distance
        min_distanced_field, min_distance = min(distances_for_koord.items(), key = lambda x:x[1])
        results.append(spec_field_numbers[min_distanced_field])
    return results

def main(n, m, special_fields):
    koords = generate_koords(n,m)
    special_fields_tuples = generate_special_fields_koords(special_fields)
    special_fields_numbers = generate_special_fields_number(special_fields_tuples)
    results = generate_distance(special_fields_numbers,koords)
    return results