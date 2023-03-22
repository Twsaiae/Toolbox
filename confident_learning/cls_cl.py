"""
Cleanlab是一个用于处理杂乱的真实数据的开源框架，它基于置信度学习的理论，可以识别数据集中的错误标注，测量数据集质量，用噪声数据训练可靠模型，并帮助管理高质量的数据集123。Cleanlab是如何根据预测结果和标签信息确定哪些是问题标签的呢？根据45，Cleanlab使用了以下步骤：

首先，对数据集进行K折交叉验证，得到每个样本在每个类别上的预测概率。
然后，根据置信度学习的公式，计算每个样本在其真实标签下的置信度（即预测概率与先验概率之积）。
最后，对每个类别下的样本按照置信度从低到高排序，并选取置信度最低的一定比例作为问题标签。
这样就可以利用Cleanlab找出错误标注的样本，并进行修正或删除。👏
"""
import os
import shutil

import numpy as np
from cleanlab.filter import find_label_issues
import json

if __name__ == '__main__':
    # p_0 = [0.9, 0.9, 0.5, 0.3, 0.3, 0.2, 0.2, 0.4, 0.5, 0.6, 0.9, 0.9, 0.5, 0.3, 0.3, 0.2, 0.2, 0.4, 0.5, 0.6, 0.9, 0.9,
    #        0.5, 0.3, 0.3, 0.2, 0.2, 0.4, 0.5, 0.6, 0.9, 0.9, 0.5, 0.3, 0.3, 0.2, 0.2, 0.4, 0.5, 0.6, 0.9, 0.9, 0.5, 0.3,
    #        0.3, 0.2, 0.2, 0.4, 0.5, 0.6, 0.9, 0.9, 0.5, 0.3, 0.3, 0.2, 0.2, 0.4, 0.5, 0.6, 0.9, 0.9, 0.5, 0.3, 0.3, 0.2,
    #        0.2, 0.4, 0.5, 0.6, 0.9, 0.9, 0.5, 0.3, 0.3, 0.2, 0.2, 0.4, 0.5, 0.6]
    # p_1 = [0.1, 0.1, 0.5, 0.7, 0.7, 0.9, 0.8, 0.7, 0.5, 0.4, 0.1, 0.1, 0.5, 0.7, 0.7, 0.9, 0.8, 0.7, 0.5, 0.4, 0.1, 0.1,
    #        0.5, 0.7, 0.7, 0.9, 0.8, 0.7, 0.5, 0.4, 0.1, 0.1, 0.5, 0.7, 0.7, 0.9, 0.8, 0.7, 0.5, 0.4, 0.1, 0.1, 0.5, 0.7,
    #        0.7, 0.9, 0.8, 0.7, 0.5, 0.4, 0.1, 0.1, 0.5, 0.7, 0.7, 0.9, 0.8, 0.7, 0.5, 0.4, 0.1, 0.1, 0.5, 0.7, 0.7, 0.9,
    #        0.8, 0.7, 0.5, 0.4, 0.1, 0.1, 0.5, 0.7, 0.7, 0.9, 0.8, 0.7, 0.5, 0.4]
    # label_origin = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0,
    #                 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1,
    #                 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    #
    # s = list()
    # psx = list()
    # for index in range(len(label_origin)):
    #     s.append(label_origin[index])
    #     psx.append(
    #         [p_0[index], p_1[index]]
    #     )
    # cl_pbc = find_label_issues(
    #     s,
    #     psx,
    #     filter_by="prune_by_class",
    #     return_indices_ranked_by="self_confidence"
    #     # prune_method='prune_by_class',
    #     # sorted_index_method='prob_given_label'
    # )
    # print("The Index of Error Samples are: {}".format(",".join([str(ele) for ele in cl_pbc])))
    project_name = '棱边'
    json_path = f'E:\pycharmproject\clean_methods\cross_clean\{project_name}_output.json'
    with open(json_path, 'r') as file:
        output = json.load(file)

    s = np.array(output['target_all'])
    psx = np.array(output['pred_all'])

    cl_pbc = find_label_issues(
        s,
        psx,
        filter_by="prune_by_class",
        return_indices_ranked_by="self_confidence"
        # prune_method='prune_by_class',
        # sorted_index_method='prob_given_label'
    )

    print("The Index of Error Samples are: {}".format(",".join([str(ele) for ele in cl_pbc])))
    print(f"一共有数据{len(output['target_all'])}，其中错误的数据有{len(cl_pbc)}")
    # bad_path = [output['img_name_list'][i] for i in cl_pbc]
    dst = f'E:\pycharmproject\clean_methods\cross_clean\src_1\{project_name}/bad'
    os.makedirs(dst, exist_ok=True)
    for idx, img_path in enumerate(output['img_name_list']):

        if idx in cl_pbc:
            src_img_path = os.path.join(r'E:\\pycharmproject\\clean_methods\\cross_clean', img_path)
            img_name = os.path.basename(src_img_path)
            dst_img_path = os.path.join(dst, img_name)
            shutil.move(src_img_path, dst_img_path)
