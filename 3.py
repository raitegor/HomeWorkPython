import os
import shutil

def shufl_dir():
    for way, direct, files in os.walk('project'):
       shutil.copytree('project', os.path.join('project', 'temp'))
       for i in direct:
           shutil.rmtree(os.path.join('project', i))

