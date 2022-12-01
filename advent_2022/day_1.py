from pathlib import Path

def get_elf_max_calorie(input:str, nb_elves:int = 1) -> list:

    data = [map(int, i.split('\n')) for i in input.split('\n\n')]
    result = [(index+1, sum(value)) for index, value in enumerate(data)]
    result.sort(key=lambda a: a[1], reverse=True)
    return result[:nb_elves]


filename_input = Path('advent_2022/data/day_1.txt')
with open(filename_input, mode='r', encoding='utf8') as infile:
    data = infile.read()

result = get_elf_max_calorie(data)
print(f"""Result challenge 1 : 
    - Elf carrying the most calories : {result[0][0]}
    - Total Calories is that Elf carrying : {result[0][1]}""")

print("-------------------------------------------------")

result = get_elf_max_calorie(data, nb_elves=3)

print(f"""Result challenge 2 : 
    - Elves carrying the most calories : {[res[0] for res in result]}
    - Total Calories is these Elves carrying : {sum([res[1] for res in result])}""")