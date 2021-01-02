import math
import tracemalloc
from multiprocessing import Pool

def generate_koords(spec_field_numbers,n,m):
    for i in range(0,n):
        for j in range(0,m):
            yield (spec_field_numbers,(i,j))

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

def generate_distance(params):
    spec_field_numbers,koord = params
    distances_for_koord = {}
    for key, _ in spec_field_numbers.items():
        distance = math.sqrt(math.pow((koord[0]-key[0]),2)+(math.pow((koord[1]-key[1]),2)))
        distances_for_koord[key] = distance
    min_distanced_field, _ = min(distances_for_koord.items(), key = lambda x:x[1])
    return spec_field_numbers[min_distanced_field]

def main(special_fields, n , m):
    special_fields_numbers = generate_special_fields_number(special_fields)
    with Pool(4) as pool:     
        r = pool.imap(generate_distance, generate_koords(special_fields_numbers,n,m), chunksize=n)
        return list(r)
