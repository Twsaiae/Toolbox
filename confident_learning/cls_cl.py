import numpy as np


from cleanlab.filter import find_label_issues

if __name__ == '__main__':
    p_0 = [0.9, 0.9, 0.5, 0.3, 0.3, 0.2, 0.2, 0.4, 0.5, 0.6, 0.9, 0.9, 0.5, 0.3, 0.3, 0.2, 0.2, 0.4, 0.5, 0.6, 0.9, 0.9,
           0.5, 0.3, 0.3, 0.2, 0.2, 0.4, 0.5, 0.6, 0.9, 0.9, 0.5, 0.3, 0.3, 0.2, 0.2, 0.4, 0.5, 0.6, 0.9, 0.9, 0.5, 0.3,
           0.3, 0.2, 0.2, 0.4, 0.5, 0.6, 0.9, 0.9, 0.5, 0.3, 0.3, 0.2, 0.2, 0.4, 0.5, 0.6, 0.9, 0.9, 0.5, 0.3, 0.3, 0.2,
           0.2, 0.4, 0.5, 0.6, 0.9, 0.9, 0.5, 0.3, 0.3, 0.2, 0.2, 0.4, 0.5, 0.6]
    p_1 = [0.1, 0.1, 0.5, 0.7, 0.7, 0.9, 0.8, 0.7, 0.5, 0.4, 0.1, 0.1, 0.5, 0.7, 0.7, 0.9, 0.8, 0.7, 0.5, 0.4, 0.1, 0.1,
           0.5, 0.7, 0.7, 0.9, 0.8, 0.7, 0.5, 0.4, 0.1, 0.1, 0.5, 0.7, 0.7, 0.9, 0.8, 0.7, 0.5, 0.4, 0.1, 0.1, 0.5, 0.7,
           0.7, 0.9, 0.8, 0.7, 0.5, 0.4, 0.1, 0.1, 0.5, 0.7, 0.7, 0.9, 0.8, 0.7, 0.5, 0.4, 0.1, 0.1, 0.5, 0.7, 0.7, 0.9,
           0.8, 0.7, 0.5, 0.4, 0.1, 0.1, 0.5, 0.7, 0.7, 0.9, 0.8, 0.7, 0.5, 0.4]
    label_origin = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0,
                    0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1,
                    1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

    s = list()
    psx = list()
    for index in range(len(label_origin)):
        s.append(label_origin[index])
        psx.append(
            [p_0[index], p_1[index]]
        )
    s = np.array(s)
    psx = np.array(psx)

    cl_pbc = find_label_issues(
        s,
        psx,
        filter_by="prune_by_class",
        return_indices_ranked_by="self_confidence"
        # prune_method='prune_by_class',
        # sorted_index_method='prob_given_label'
    )
    print("The Index of Error Samples are: {}".format(",".join([str(ele) for ele in cl_pbc])))
































    # # STEP 0 构建输入样本
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
    # # # 构建DataFrame
    # # dict_data = {
    # #     "j=0": p_0,
    # #     "j=1": p_1,
    # #     "label_origin==0": label_origin,
    # # }
    # # df_data = pd.DataFrame(dict_data)
    # # # print(df_data)
    # #
    # # # STEP 1 计算标签阈值
    # # list_0 = list()
    # # list_1 = list()
    # # for index, column in df_data.iterrows():
    # #     if column["label_origin==0"] == 0:
    # #         list_0.append(column["j=0"])
    # #     if column["label_origin==0"] == 1:
    # #         list_1.append(column["j=1"])
    # # # 前五条记录的人工标签是0，所以j==0的阈值是前五条记录，在类别为0的概率平均值
    # # average_p_0 = np.mean(list_0)
    # # # 后五条记录的人工标签是1，所以j==1的阈值是后五条记录，在类别为1的概率平均值
    # # average_p_1 = np.mean(list_1)
    # #
    # # # print("The thresholds of [j==0] is {} and [j==1] is {}".format(average_p_0, average_p_1))
    # #
    # # # STEP 2 计算联合统计分布矩阵
    # # dict_co_count = {
    # #     "true_0": [0, 0],
    # #     "true_1": [0, 0],
    # # }
    # #
    # # df_co_count = pd.DataFrame(dict_co_count, index=["pred_0", "pred_1"])
    # # # print(df_co_count)
    # #
    # # for index in range(len(label_origin)):
    # #     if p_0[index] > p_1[index] and p_0[index] > average_p_0:
    # #         if label_origin[index] == 0:
    # #             df_co_count.loc["pred_0", "true_0"] = df_co_count.at["pred_0", "true_0"] + 1
    # #         if label_origin[index] == 1:
    # #             df_co_count.loc["pred_1", "true_0"] = df_co_count.at["pred_1", "true_0"] + 1
    # #     if p_1[index] > p_0[index] and p_1[index] > average_p_1:
    # #         if label_origin[index] == 1:
    # #             df_co_count.loc["pred_1", "true_1"] = df_co_count.at["pred_1", "true_1"] + 1
    # #         if label_origin[index] == 0:
    # #             df_co_count.loc["pred_0", "true_1"] = df_co_count.at["pred_0", "true_1"] + 1
    # # # print(df_co_count)
    # #
    # # # STEP 3 校准数据分布
    # # num_label_origin_0, num_label_origin_1 = 10, 10
    # #
    # # for index, column in df_co_count.iterrows():
    # #     y_i_j = column["true_0"] + column["true_1"]
    # #     df_co_count.loc[index, 'true_0'] = num_label_origin_0 * column["true_0"] / y_i_j
    # #     df_co_count.loc[index, 'true_1'] = num_label_origin_0 * column["true_1"] / y_i_j
    # #
    # # # print(df_co_count)
    # #
    # # # STEP 4 计算置信度联合概率分布矩阵
    # # dict_co_prob = {
    # #     "true_0": [0., 0.],
    # #     "true_1": [0., 0.],
    # # }
    # # df_co_prob = pd.DataFrame(dict_co_prob, index=["pred_0", "pred_1"])
    # # # print(df_co_prob)
    # #
    # # total = 0
    # # for column in ["pred_0", "pred_1"]:
    # #     for row in ["true_0", "true_1"]:
    # #         total += df_co_count.at[column, row]
    # #
    # # # print("分母是【{}】".format(total))
    # #
    # # for column in ["pred_0", "pred_1"]:
    # #     for row in ["true_0", "true_1"]:
    # #         df_co_prob.loc[column, row] = df_co_count.at[column, row] / total
    # # # print(df_co_prob)
    #
    # # STEP 5 找出标签错误样本
    #
    # # 输入
    # # s:噪声标签
    # # psx: n x m 的预测概率概率，通过交叉验证获得
    # s = list()
    # psx = list()
    # for index in range(len(label_origin)):
    #     s.append(label_origin[index])
    #     psx.append(
    #         [p_0[index], p_1[index]]
    #     )
    # s = np.array(s)
    # psx = np.array(psx)
    # # Method 3：Prune by Class (PBC)
    #
    # cl_pbc = find_label_issues(
    #     s,
    #     psx,
    #     filter_by="prune_by_class",
    #     return_indices_ranked_by="self_confidence"
    #     # prune_method='prune_by_class',
    #     # sorted_index_method='prob_given_label'
    # )
    # print("The Index of Error Samples are: {}".format(",".join([str(ele) for ele in cl_pbc])))
    #
    # # # Method 4：Prune by Noise Rate (PBNR)
    # # cl_pbnr = find_label_issues(
    # #     s,
    # #     psx,
    # #     filter_by="prune_by_class",
    # #     return_indices_ranked_by="self_confidence"
    # # )
    # # print("The Index of Error Samples are: {}".format(",".join([str(ele) for ele in cl_pbnr])))
    # # # Method 5：C+NR
    # # cl_both = find_label_issues(
    # #     s,
    # #     psx,
    # #     filter_by="prune_by_class",
    # #     return_indices_ranked_by="self_confidence"
    # # )
    # # print("The Index of Error Samples are: {}".format(",".join([str(ele) for ele in cl_both])))
