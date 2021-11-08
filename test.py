import data

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

d = data.Data()
data = d.parsing_buildprop('build.prop')
print(data)


