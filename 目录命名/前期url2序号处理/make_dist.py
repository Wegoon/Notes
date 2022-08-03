file_r = open(r'D:\aDesktop\tmp\a.csv', 'r', encoding = 'utf-8')
file_w = open(r'D:\aDesktop\tmp\d.csv', 'w', encoding = 'utf-8')
url_id_dict = {}
for line in file_r.readlines():
    key, val = line.strip().split(',')
    if key in url_id_dict:
        url_id_dict[key] += '-' + val
    else:
        url_id_dict[key] = val
print(len(url_id_dict))
for key in url_id_dict:
    # print(key, url_id_dict[key])
    # print('"' + key + '"' + ' : ' + '"' + url_id_dict[key] + '"' + ',')
    file_w.write('"' + key + '"' + ' : ' + '"' + url_id_dict[key] + '"' + ',\n')