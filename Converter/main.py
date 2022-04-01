
user_input = input("Please, write the file you want to process: ")
f = open(user_input, 'r+')


def convert(mass_lb):
    kilo = float(mass_lb) * 0.45
    return round(kilo, 2)


with open("pounds.txt", 'r') as file:
    mass_data = file.readlines()
    first_mass = mass_data[0]
    second_mass = mass_data[1]
    third_mass = mass_data[2]
    fourth_mass = mass_data[3]
    fifth_mass = mass_data[4]

    first_kilogram = convert(first_mass)
    second_kilogram = convert(second_mass)
    third_kilogram = convert(third_mass)
    fourth_kilogram = convert(fourth_mass)
    fifth_kilogram = convert(fifth_mass)

    total_kilograms = [first_kilogram, second_kilogram, third_kilogram, fourth_kilogram, fifth_kilogram]
    total_number_kilograms = sum(total_kilograms)

    print(f'Line 1: {first_mass} pounds -> {first_kilogram} Kilograms')
    print(f'Line 2:  {second_mass} pounds -> {second_kilogram} Kilograms')
    print(f'Line 3: {third_mass} pounds -> {third_kilogram} Kilograms')
    print(f'Line 4: {fourth_mass} pounds -> {fourth_kilogram} Kilograms')
    print(f'Line 5: {first_mass} pounds -> {fifth_kilogram} Kilograms')

    print(f'Total number of Kilograms: {total_number_kilograms}')

with open("Output.txt", "a") as save_data:
    Line1 = f'{first_kilogram} \n'
    Line2 = f'{second_kilogram} \n'
    Line3 = f'{third_kilogram} \n'
    Line4 = f'{fourth_kilogram} \n'
    Line5 = f'{fifth_kilogram} \n'

    save_data.writelines([Line1, Line2, Line3, Line4, Line5])



































