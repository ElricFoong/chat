def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig')as f:
        for line in f:
            lines.append(line.strip().split(' '))
    return lines


def convert(lines):
    time = []
    name = []
    for line in lines:
        time.append(line[0][:5])
        name.append(line[0][5:])
    print(time, name)


lines = read_file('3.txt')
convert(lines)
