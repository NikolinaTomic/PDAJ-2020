import math
import tracemalloc

def generate_koords(n,m):
    for i in range(0,n):
        for j in range(0,m):
            yield (i,j)

def generate_special_fields_koords(special_field):
    koords = []
    special_field = special_field.split(",")
    for i in special_field:
        koords.append(int(i))
    yield tuple(koords)

def generate_special_fields_number(special_fields):
    spec_field_numbers = {}
    i = 0
    for special_field in special_fields:
        spec_field_numbers[next(generate_special_fields_koords(special_field))] = i
        i = i + 1
    return spec_field_numbers

def generate_distance(n,m,special_fields):
    koords = generate_koords(n,m)
    special_fields_numbers = generate_special_fields_number(special_fields)
    results = []
    for koord in koords:
        distances_for_koord = {}
        for key,value in special_fields_numbers.items():
            distance = math.sqrt(math.pow((koord[0]-key[0]),2)+(math.pow((koord[1]-key[1]),2)))
            distances_for_koord[key] = distance
        min_distanced_field, min_distance = min(distances_for_koord.items(), key = lambda x:x[1])
        yield special_fields_numbers[min_distanced_field]

def main(n, m , special_fields):
    results = generate_distance(n,m,special_fields)
    return list(results)
