csv = open('csv_data.txt', 'r')
lines = csv.readlines()
csv.close()

lines = [line.strip() for line in lines[1:]]

data = []
for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f'{name} is {age}, studying {degree} at {university}')


sample_csv_value = ','.join(['Fadilah', '19', 'UNIBEN', 'Computer Science'])
print(sample_csv_value)