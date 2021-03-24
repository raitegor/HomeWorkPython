import os
import django
from collections import defaultdict

root_dir = django.__path__[0]
django_files = {}
from os.path import relpath

def django():
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            ext = file.rsplit('.', maxsplit=1)[-1]
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            if size in django_files:
                django_files[size][0] += 1
                if ext not in django_files[size][1]:
                    django_files[size][1].append(ext)
            else:
                django_files[size] = [1, [ext]]

    for size, nums in sorted(django_files.items()):
        print(f'{size}:{tuple(nums)}')


