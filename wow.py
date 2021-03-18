import os
direct = []
with open ('config.yaml', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split('/n')[0]
        if line.find('-') < 0:
            if not os.path.exists(line):
                os.makedirs(line)
                direct.append(line)

        if line.rfind('-') == 0 and line.find('.') < 0:
            if not os.path.exists(os.path.join(direct[0], line)):
                os.mkdir(os.path.join(direct[0], line[1:]))
                direct.append(line[1:])

        if line.rfind('-') == 1 and line.find('.') > 0:
            with open(os.path.join(direct[0], direct[-1]), 'w', encoding='utf-8') as new_f:
                new_f.write('')


print(direct)


