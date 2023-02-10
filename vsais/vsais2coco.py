import json
import os
import numpy as np


def convert_to_soil_cover_format(save_to, raw_json_path):
    coco = {
        # "info": INFO,
        # "licenses": LICENSES,
        "categories": [],
        "images": [],
        "annotations": []
    }
    # categories 与常规的coco不同，color信息也存入了，
    my_json = json.load(open(raw_json_path, encoding='utf-8'))
    l = my_json["label_category"]
    c = []
    # 去除others类别
    for j in range(len(l)):
        # print(c[j]["name"])
        if l[j]["name"] != "others":
            c.append(l[j])
    coco["categories"] = c

    i_num = 1
    a_num = 0
    for image in my_json["images"]:
        w = image["width"]
        h = image["height"]
        # images
        i = {
            "id": i_num,
            "file_name": image["filename"],
            "width": image["width"],
            "height": image["height"]
        }
        coco["images"].append(i)

        # annotations 一个类别放一起,首先遍历所有类别，类别已经去除了所有others
        for j in range(len(c)):
            c_id = c[j]["id"]
            x_min = float('inf')
            y_min = float('inf')
            x_max = 0
            y_max = 0
            bbox = []
            segmentation = []
            for label in image["label"]:
                if label["category_id"] == c_id:
                    # 先不加area试一下，不好算
                    # 计算bbox和segmentation
                    shape = [[w, h]]
                    shape = np.array(shape)

                    a = np.array(label["coordinate"])
                    d = shape * a
                    d = np.around(d, decimals=1)
                    a_list = d.tolist()

                    seg = []
                    for i in a_list:
                        x_min = i[0] if x_min > i[0] else x_min
                        x_max = i[0] if x_max <= i[0] else x_max
                        y_min = i[1] if y_min >= i[1] else y_min
                        y_max = i[1] if y_max <= i[1] else y_max
                        for k in i:
                            seg.append(k)
                    bbox = [x_min, y_min, x_max, y_max]
                    segmentation.append(seg)

            if segmentation:
                a_num += 1
                a = {
                    "id": a_num,
                    "image_id": i_num,
                    "category_id": c_id,
                    "iscrowd": 0,
                    "bbox": bbox,
                    "segmentation": segmentation
                }
                coco["annotations"].append(a)
        i_num += 1

    filename = os.path.join(save_to, 'coco.json')

    with open(filename, 'w') as output_json_file:
        json.dump(coco, output_json_file, indent=4, ensure_ascii=False)

    return filename


if __name__ == '__main__':
    pass