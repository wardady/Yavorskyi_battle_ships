import random


def read_field(filename):
    field = []
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            field.append(list(line.strip('\n')))
    return field


def ship_size(data, cords):
    size = 0
    if has_ship(data, cords):
        size += 1
        newcord = (chr(ord(cords[0]) + 1), cords[1])
        while ord(newcord[0]) < 75 and has_ship(data, newcord):
            size += 1
            newcord = (chr(ord(newcord[0]) + 1), cords[1])
        newcord = (chr(ord(cords[0]) - 1), cords[1])
        while ord(newcord[0]) >= 65 and has_ship(data, newcord):
            size += 1
            newcord = (chr(ord(newcord[0]) - 1), cords[1])
        newcord = (chr(ord(cords[0])), cords[1] + 1)
        while newcord[1] < 10 and has_ship(data, newcord):
            size += 1
            newcord = (chr(ord(newcord[0])), cords[1] + 1)
        newcord = (chr(ord(cords[0])), cords[1] - 1)
        while newcord[1] >= 0 and has_ship(data, newcord):
            size += 1
            newcord = (chr(ord(newcord[0])), cords[1] - 1)
    return size


def has_ship(data, cords):
    if data[65 - ord(cords[0].upper())][cords[1]] != ' ':
        return True
    return False


def is_valid(data):
    count = 0
    for row in data:
        for cell in row:
            if cell == '*':
                count += 1
    if count != 20:
        return False


def field_to_str(data):
    out = ''
    for row in data:
        out += ''.join(row) + '\n'
    return out


def generate_field():
    ships = []
    field = [['' for j in range(10)] for i in range(10)]
    field, cords = generate_ship(4, field)
    ships.append(cords)
    for i in range(2):
        field, cords = generate_ship(3, field)
        ships.append(cords)
    for i in range(3):
        field, cords = generate_ship(2, field)
        ships.append(cords)
    for i in range(4):
        field, cords = generate_ship(1, field)
        ships.append(cords)
    for row in field:
        for i in range(len(row)):
            if row[i] == '':
                row[i] = ' '
    return field, ships


def generate_ship(size, field):
    horizontal = random.randint(0, 1)
    x, y = 0, 0
    if horizontal:
        while True:
            x, y = random.randint(0, 10 - size), random.randint(0, 10)
            if check_ship(x, y, horizontal, size, field):
                break
        for i in range(size):
            field[y][x + i] = '*'
        field = field_blank_cells(x, y, horizontal, size, field)
    else:
        while True:
            x, y = random.randint(0, 9), random.randint(0, 10 - size)
            if check_ship(x, y, horizontal, size, field):
                break
        for i in range(size):
            field[y + i][x] = '*'
        field = field_blank_cells(x, y, horizontal, size, field)
    return field, (x, y, horizontal,size)


def check_ship(x, y, hor, size, field):
    try:
        if hor:
            for i in range(size):
                if field[y][x + i] != '':
                    return False
            return True
        else:
            for i in range(size):
                if field[y + i][x] != '':
                    return False
            return True
    except:
        return False


def field_blank_cells(x, y, hor, size, field):
    if hor:
        if x != 10 - size and x != 0:
            field[y][x - 1] = ' '
            field[y][x + size] = ' '
        elif x == 0:
            field[y][x + size] = ' '
        else:
            field[y][x - 1] = ' '

        if y != 0 and y != 9:
            field = upper_line(x, y, size, field)
            field = lower_line(x, y, size, field)
        elif y == 0:
            field = lower_line(x, y, size, field)
        else:
            field = upper_line(x, y, size, field)
    else:
        if y != 10 - size and y != 0:
            field[y - 1][x] = ' '
            field[y + size][x] = ' '
        elif y == 0:
            field[y + size][x] = ' '
        else:
            field[y - 1][x] = ' '

        if x != 0 and x != 9:
            field = lef_line(x, y, size, field)
            field = right_line(x, y, size, field)
        elif x == 0:
            field = right_line(x, y, size, field)
        else:
            field = lef_line(x, y, size, field)
    return field


def lef_line(x, y, size, field):
    if y != 10 - size and y != 0:
        for i in range(size + 2):
            field[y - 1 + i][x - 1] = ' '
    elif y == 0:
        for i in range(size + 1):
            field[y + i][x - 1] = ' '
    else:
        for i in range(size + 1):
            field[y + i - 1][x - 1] = ' '
    return field


def right_line(x, y, size, field):
    if y != 10 - size and y != 0:
        for i in range(size + 2):
            field[y - 1 + i][x + 1] = ' '
    elif y == 0:
        for i in range(size + 1):
            field[y + i][x + 1] = ' '
    else:
        for i in range(size + 1):
            field[y + i - 1][x + 1] = ' '
    return field


def upper_line(x, y, size, field):
    if x != 10 - size and x != 0:
        for i in range(size + 2):
            field[y - 1][x - 1 + i] = ' '
    elif x == 0:
        for i in range(size + 1):
            field[y - 1][x + i] = ' '
    else:
        for i in range(size + 1):
            field[y - 1][x + i - 1] = ' '
    return field


def lower_line(x, y, size, field):
    if x != 10 - size and x != 0:
        for i in range(size + 2):
            field[y + 1][x - 1 + i] = ' '
    elif x == 0:
        for i in range(size + 1):
            field[y + 1][x + i] = ' '
    else:
        for i in range(size + 1):
            field[y + 1][x + i - 1] = ' '

    return field
