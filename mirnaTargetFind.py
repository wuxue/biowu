#-*- coding:gbk -*-
'''
����ű����ڴ���miRNA�л����ϵ�ԣ�
�������ڴ��� �ˡ�С�󡢴���İл���Ԥ���ϵ
'''

from os import path
import mybio


def getDataPath(org):
    filePath = path.realpath(mybio.__file__)    
    dataDir = path.join(path.split(filePath)[0], 'data', 'miRNATargets', org)
    return dataDir
    
def query(mirs):
    