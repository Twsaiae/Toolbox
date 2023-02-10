"""
34类darknet标签转换成4类密闭运输标签
"""
import os

path = '/home/vs/PycharmProjects/automatic/project/CLT34_20220308/ori/labels'
dst = '/home/vs/PycharmProjects/automatic/project/CLT34_20220308/ori/labels_gld'
os.makedirs(dst,exist_ok=True)

# for _, _, files in os.walk(path):
for f in os.listdir(path):
    txt_path = os.path.join(path, f)
    dst_path = os.path.join(dst, f)
    with open(txt_path, "r") as txt:
        lines = txt.readlines()
    result = []
    for i in lines:
        if i[0] is None:
            result.append(None)
        # 货车从这一刻起，就变成了土方车
        if i[0] == '0':  # 货车
            result.append("0" + i[1:])
        if i[0] == '3':  # 土方车
            if i[1].isdigit():
                continue
            else:
                result.append("0" + i[1:])
        if i[0] == '1' and i[1] == '1':  # 货车——有货
            result.append("2" + i[2:])
        if i[0] == '1' and i[1] == '2':  # 货车——无货
            result.append("2" + i[2:])
        elif i[0] == '1' and i[1] == '4':  # 土方车车斗_闭
            result.append("1" + i[2:])
        elif i[0] == '1' and i[1] == '5':  # 土方车车斗_开
            result.append("2" + i[2:])
        elif i[0] == '1' and i[1] == '6':  # 土方车车斗_未完全开
            result.append("3" + i[2:])
    with open(dst_path, "w") as file:
        file.writelines(result)
