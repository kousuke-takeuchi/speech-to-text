import os
import random
import string

import dotenv


'''.envファイルに記載の認証情報をロードする
'''
def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
    dotenv.load_dotenv(dotenv_path)


'''n桁のランダム文字列を作成する
'''
def random_string(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(randlst)
