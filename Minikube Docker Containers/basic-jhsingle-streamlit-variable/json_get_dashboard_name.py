import os
import json

#os.environ['DASHBOARD'] = str(dict_in['dashboard'])
def getDashboard():
    dict_in = json.loads(os.environ["USER_OPTIONS"].replace("'", '"'))
    # dict_in = {"dashboard":"sliderAdd.py"}
    print(str(dict_in['dashboard']))

if __name__ == '__main__':
    getDashboard()