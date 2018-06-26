import json
import os
from conf import setting


def save(user_dic):
    user_path = os.path.join(setting.BASE_DB, '%s.json' % user_dic['name'])
    with open(user_path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f)
        f.flush()

def select(name):
    user_path = os.path.join(setting.BASE_DB, '%s.json' % name)
    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return None
