import os
import csv


def delete_column(csv_file_name, column_indices_to_remove=[]):
    with open(csv_file_name, "r", encoding='utf8') as file_in:
        reader = csv.reader(file_in)
        with open('temp.csv', "w", encoding='utf8') as file_out:
            writer = csv.writer(file_out)
            for row in reader:
                row = [row[i] for i in range(len(row)) if i not in column_indices_to_remove]
                writer.writerow(row[1:3])
    os.remove(csv_file_name)
    os.rename('temp.csv', csv_file_name)


def remove_newlines(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        with open('temp.csv', 'w', encoding='utf8') as file2:
            for line in file:
                if not line.isspace():
                    file2.write(line)

    os.remove(file_name)
    os.rename('temp.csv', file_name)
