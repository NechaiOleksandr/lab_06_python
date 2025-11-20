input_filename = 'numbers.txt'
output_filename = 'sum_numbers.txt'

sum = 0

with open(input_filename, 'r') as f:
    for number in f:
        sum += float(number)

print(f"Сума чисел: {sum}")

with open(output_filename, 'w') as f_out:
    f_out.write(str(sum))

print(f"Суму успішно записано у файл '{output_filename}'")