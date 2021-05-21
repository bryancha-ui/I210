def table_print(headers, data, width=10):
    [h1, h2] = headers
    fmt = "{:<{}} {:<{}}"
    print(fmt.format(h1, width, h2, width))
    [print(fmt.format(row[0], width, row[1], width)) for row in data]


def selection_sort(values, pos):
    n = len(values)
    for i in range(0, n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if values[j][pos] > values[min_idx][pos]:
                min_idx = j
        values[i], values[min_idx] = values[min_idx], values[i]
    return values


def tallied_data(user_list, col_query, col_tally):
    workout = dict()
    for d in user_list:
        if d[col_query] not in workout:
            workout[d[col_query]] = 0
        workout[d[col_query]] += int(d[col_tally])

    workout = selection_sort(list(workout.items()), 1)
    return workout
