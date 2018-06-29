import subprocess
import collections
import os.path as osp

from config import config

Ques = collections.namedtuple(
    'Ques',['type','year','month','day','time','name'])


class Ques_Set:

    def __init__(self):
        self._Ques_set = []

    def add_Ques(self, qtype, year, month, day, time, name):
        self._Ques_set.append(Ques(qtype,year,month,day,time,name))

    def get_Ques(self):
        for code in config['QUES']['available'].split(','):
            path = osp.join(osp.abspath(osp.dirname(__file__)),code)
            ques_info = subprocess.check_output(
                ['ls','-l','--full-time',path]).decode('utf-8').split()[2:]
            for i in range(0,len(ques_info),9):
                year, month, day = ques_info[i+5].split('-')
                Ques_Set.add_Ques(self, code, year, month, day, ques_info[i+6],
                    ques_info[i+8])

    def __len__(self):
        return len(self._Ques_set)

    def __getitem__(self, position):
        return self._Ques_set[position]

def main():
    q = Ques_Set()
    q.get_Ques()
    print(q[:])


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
