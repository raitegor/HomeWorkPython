import os
dir_name = ['settings', 'mainapp', 'adminapp', 'authapp']

def create_dir(dir_name):
    dir_path = os.path.join('my_project', dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

for i in dir_name:
    create_dir(i)