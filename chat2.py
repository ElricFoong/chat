def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig')as f:
        for line in f:
            chat.append(line.strip())
    return chat


def convert(chat):

    allen_wc = 0
    allen_sc = 0
    allen_pc = 0
    viki_wc = 0
    viki_sc = 0
    viki_pc = 0
    for line in chat:
        line = line.split(' ')
        time = line[0]
        name = line[1]
        if name == 'Allen':
            if line[2] == '貼圖':
                allen_sc += 1
            elif line[2] == '圖片':
                allen_pc += 1
            for m in line[2:]:
                allen_wc += len(m)
        elif name == 'Viki':
            if line[2] == '貼圖':
                viki_sc += 1
            elif line[2] == '圖片':
                viki_pc += 1
            for m in line[2:]:
                viki_wc += len(m)
    print('allen said ', allen_wc)
    print('allen sticker ', allen_sc)
    print('allen picture ', allen_pc)
    print('viki said ', viki_wc)
    print('viki sticker ', viki_sc)
    print('viki picture ', viki_pc)


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)


main()
