from sys import argv

with open ('bakery.csv', 'a', encoding='utf-8') as add:
    with open('bakery.csv', 'r', encoding='utf-8') as show:
        if len(argv) == 1:
            print(show.read())
        elif len(argv) == 2:
            if ',' in argv[1]:
                show.read()
                print(argv[1], file=add)
            else:
                print(*show.readlines()[int(argv[1]) - 1:], sep='')
        else:
            print(*show.read().split()[int(argv[1]):int(argv[2]) + 1], sep='\n')



