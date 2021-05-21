import os
import csv
import sys
from mymod import *


def readfile(filename):
    try:
        with open(filename, newline='', mode='r') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]
    except IOError:
        sys.exit('Please check the file name and path..')


def write_file(filename, headers, contents, width=30, mode='w'):
    fmt = "{:<{}} {:<{}} {:<{}} {:<{}}\n"
    if os.path.exists(filename):
        mode = 'a'

    with open(filename, newline='', encoding='utf-8', mode=mode) as f:
        if mode == 'w':
            f.write(fmt.format(headers[0], width, headers[1], width, headers[2], width, headers[3], width))

        for content in contents:
            f.write(fmt.format(content[0], width, content[1], width, content[2], width, content[3], width))


def readline_for_year(filename, year):
    csvfile = readfile(filename)
    year_list = [list(row.values()) for row in csvfile if year == row['YEAR']]

    if len(year_list) == 0:
        sys.exit('Enter Valid Year.')

    print(len(csvfile),"rows")
    print('Data loaded')

    return year_list


def q_a(filename, year):
    data = readline_for_year(filename, year)
    table_print(['CANDIDATE', 'TOTALVOTES'], tallied_data(data, 3, 7), 30)


def q_b(filename, year):
    data = readline_for_year(filename, year)
    table_print(['PARTY', 'TOTALVOTES'], tallied_data(data, 4, 7), 30)


def q_c(filename, year):
    data = readline_for_year(filename, year)
    for d in data:
        d[5] = 1 if d[5] == 'TRUE' else 0

    table_print(['YEAR', 'WRITEIN'], tallied_data(data, 0, 5), 30)


def q_d(filename, year):
    data = readline_for_year(filename, year)
    win_data = selection_sort(data, 6)[0]
    table_print(['YEAR', 'CANDIDATE'], [[win_data[0], win_data[3]]], 30)


def find_party(data, candidate):
    for d in data:
        if d[3] == candidate:
            return d[4]
    return ''


def bonus(filename, year):
    data = readline_for_year(filename, year)
    # print(data)
    each_candidate_votes = tallied_data(data, 3, 6)
    print(each_candidate_votes)

    year_total_votes = 0
    for candidate in each_candidate_votes:
        year_total_votes += int(candidate[1])
    print(year_total_votes)

    final_data = []
    for candidate in each_candidate_votes:
        final_data.append([find_party(data, candidate[0]), candidate[0], candidate[1], (int(candidate[1]) / int(year_total_votes) * 100)])
    print(final_data)

    header = ['PARTY', 'CANDIDATE', 'VOTES', 'VOTES_PERCENT'];

    file_print = input('Do you want to save as file?(Y/N) > ')
    if file_print == 'Y':
        write_filename = input('Enter filename to save.')
        write_file(write_filename + '.txt', header, final_data)

    fmt = "{:<{}} {:<{}} {:<{}} {:<{}}\n"
    width = 30
    print(fmt.format(header[0], width, header[1], width, header[2], width, header[3], width))
    [print(fmt.format(d[0], width, d[1], width, d[2], width, d[3], width)) for d in final_data]


if __name__ == "__main__":
    [filename, year] = input('Enter filename and year > ').split(' ')

    while True:
        choose = input('Please choose OPTION A, B, C, or D:')
        if choose == 'a':
            print('=' * 80)
            q_a(filename, year)
            print()
        elif choose == 'b':
            print('=' * 80)
            q_b(filename, year)
            print()
        elif choose == 'c':
            print('=' * 80)
            q_c(filename, year)
            print()
        elif choose == 'd':
            print('=' * 80)
            q_d(filename, year)
            print()
        elif choose == 'bonus':
            print('=' * 80)
            bonus(filename, year)
            print()
        elif choose == 'exit':
            print()
            sys.exit('close program')
        else:
            print()
            print('wrong input.')
            print()
