file_r = open(r'D:\aDesktop\tmp\b.csv', 'r', encoding = 'utf-8')
file_w = open(r'D:\aDesktop\tmp\c.csv', 'w', encoding = 'utf-8')
for line in file_r.readlines():
    line = line.strip().strip(',').strip()
    tmp_list = line.split('/')
    file_w.write(tmp_list[2] + '\n')