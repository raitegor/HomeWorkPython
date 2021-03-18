import yaml
import os

with open('config.yaml') as f:
    content = yaml.safe_load(f)

def create_path(content, path_line=''):
        for direct, path in content.items():
            way_to_hell = os.path.join(path_line, direct)
            if not os.path.exists(way_to_hell):
                os.makedirs(way_to_hell)
            if type(path) == dict:
                create_path(path, way_to_hell)
            else:
                for i in path:
                    with open(os.path.join(way_to_hell, f'{i}'), 'w', encoding='utf-8') as new_f:
                        pass




if __name__ == '__main__':
    create_path(content)