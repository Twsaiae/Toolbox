import os

src = r'C:\Users\Thor\Downloads\大面\测试\数据集2_placed_well\test'
src2 = r'C:\Users\Thor\Downloads\大面\测试\数据集1'

for cls_name in os.listdir(src):
    cls_path = os.path.join(src, cls_name)
    for img_name in os.listdir(cls_path):
        src2_img_path = f"{src2}/{cls_name}/{img_name}"
        os.remove(src2_img_path)
# need_delete = []
# for cls_name in os.listdir(src):
#     cls_path = os.path.join(src, cls_name)
#     for img_name in os.listdir(cls_path):
#         need_delete.append(img_name)
#         # src2_img_path = f"{src2}/{cls_name}/{img_name}"
#         # os.remove(src2_img_path)
#
# for cls in os.listdir(src2):
#     cls_path = os.path.join(src2, cls)
#     for img_name in os.listdir(cls_path):
#         if img_name in need_delete:
#             img_path = os.path.join(cls_path, img_name)
#             os.remove(img_path)

# 454+2208=2662