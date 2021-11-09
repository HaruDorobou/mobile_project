import data
from xml.etree.ElementTree import parse
import numpy as np

# f = open('persistent_properties', 'r', encoding='euc-kr')
# f = open('build.prop', 'r')
# f = open('build.prop', 'r', encoding='utf-8')
#
# fs = f.readlines()
#
# for line in fs:
#
#     line = line[:-1].split('=', 2)
#     if line[0] == 'net.bt.name':
#         s1 = line[1]
#     if line[0] == 'ro.build.version.release':
#         s2 = line[1]
#
# s = s1 + s2
# print(s)

# d = data.Data()
# data = d.parsing_buildprop('build.prop')
# print(data)

tree = parse('./data/WifiConfigStore.xml')
root = tree.getroot()

# WifiConfigStoreData = root.findall('WifiConfigStoreData')
# # NetworkList = WifiConfigStoreData.findall('NetworkList')
# print(WifiConfigStoreData)
# print(root)
cols = [['SSID', 'CreationTime']]
row = []
data = np.array(cols)
for string in root.iter('string'):
    if string.attrib['name'] == 'SSID':
        row = np.array([string.text[1:-1]])
    if string.attrib['name'] == 'CreationTime':
        row = np.append(row, np.array([string.text]))
        data = np.append(data, [row], axis=0)

print(data)
