import os
import re
import numpy as np
import matplotlib.pyplot as plt


def parse_txt(txt_path):
    train_loss, val_pre, test_pre = [], [], []
    with open(txt_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('train_loss_record:'):
                train_loss = re.findall(r'\d+\.\d+', line)
                train_loss = [float(x) for x in train_loss]
            elif line.startswith('val_pre_record:'):
                val_pre = re.findall(r'\d+\.\d+', line)
                val_pre = [float(x) for x in val_pre]
            elif line.startswith('test_pre_record:'):
                test_pre = re.findall(r'\d+\.\d+', line)
                test_pre = [float(x) for x in test_pre]
    return train_loss, val_pre, test_pre


if __name__ == '__main__':
    # src = r'E:\pycharmproject\cleantest\runs5\log'
    # txt_paths_all = []
    # for txt_name in os.listdir(src):
    #     txt_paths_all.append(os.path.join(src, txt_name))

    # txt_paths = [r'E:\pycharmproject\cleantest\runs7\log\大面红外线光长条气泡_cleantest_200epochs_1.txt',
    #              r'E:\pycharmproject\cleantest\runs7\log\大面红外线光长条气泡_cleantest_200epochs_2.txt',
    #              r'E:\pycharmproject\cleantest\runs7\log\大面红外线光长条气泡_cleantest_200epochs_3.txt',
    #              r'E:\pycharmproject\cleantest\runs7\log\大面红外线光长条气泡_cleantest_200epochs_4.txt',
    #              r'E:\pycharmproject\cleantest\runs7\log\大面红外线光长条气泡_cleantest_200epochs_5.txt',
    #              r'E:\pycharmproject\cleantest\runs7\log\大面红外线光长条气泡_cleantest_200epochs_clean.txt']  # 将文件路径放在一个列表中
    txt_paths = [r'E:\pycharmproject\cleantest\runs9\log\极柱_NEG3_cleantest_200epochs_1.txt',
                 r'E:\pycharmproject\cleantest\runs9\log\极柱_NEG3_cleantest_200epochs_2.txt',
                 r'E:\pycharmproject\cleantest\runs9\log\极柱_NEG3_cleantest_200epochs_3.txt',
                 r'E:\pycharmproject\cleantest\runs9\log\极柱_NEG3_cleantest_200epochs_4.txt',
                 r'E:\pycharmproject\cleantest\runs9\log\极柱_NEG3_cleantest_200epochs_5.txt',
                 r'E:\pycharmproject\cleantest\runs9\log\极柱_NEG3_cleantest_200epochs_clean.txt']  # 将文件路径放在一个列表中
    train_losses, val_pres, test_pres = [], [], []
    for txt_path in txt_paths:
        train_loss, val_pre, test_pre = parse_txt(txt_path)
        train_losses.append(train_loss)
        val_pres.append(val_pre)
        test_pres.append(test_pre)
    print(train_losses, '\n', len(train_losses), len(train_losses[0]))
    print(val_pres, '\n', len(val_pres), len(val_pres[0]))
    print(test_pres, '\n', len(test_pres), len(test_pres[0]))

    x = np.arange(1, len(test_pres[0]) + 1, 1)

    # # TRAIN LOSS
    fig, ax1 = plt.subplots()  # 创建图实例
    ax1.plot(x, train_losses[0], label='train_loss_1')  # 作y1 = x 图，并标记此线名为linear
    ax1.plot(x, train_losses[1], label='train_loss_2')  # 作y1 = x 图，并标记此线名为linear
    ax1.plot(x, train_losses[2], label='train_loss_3')  # 作y1 = x 图，并标记此线名为linear
    ax1.plot(x, train_losses[3], label='train_loss_4')  # 作y1 = x 图，并标记此线名为linear
    ax1.plot(x, train_losses[4], label='train_loss_5')  # 作y1 = x 图，并标记此线名为linear
    ax1.plot(x, train_losses[5], 'k', label='train_loss_clean')  # 作y1 = x 图，并标记此线名为linear

    ax1.set_xlabel('epochs')  # 设置x轴名称 x label
    ax1.set_ylabel('train_loss')  # 设置y轴名称 y label
    ax1.set_title('Training Loss')  # 设置图名为Simple Plot
    ax1.legend()  # 自动检测要在图例中显示的元素，并且显示
    plt.savefig("traing_loss.jpg")

    plt.show()  # 图形可视化

    # VALID PRECISION
    fig2, ax2 = plt.subplots()  # 创建图实例
    ax2.plot(x, val_pres[0], label='val_acc_1')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax2.plot(x, val_pres[1], label='val_acc_2')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax2.plot(x, val_pres[2], label='val_acc_3')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax2.plot(x, val_pres[3], label='val_acc_4')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax2.plot(x, val_pres[4], label='val_acc_5')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax2.plot(x, val_pres[5], 'k', label='val_acc_clean')  # 作y2 = x^2 图，并标记此线名为quadratic

    ax2.set_xlabel('epochs')  # 设置x轴名称 x label
    ax2.set_ylabel('val_acc')  # 设置y轴名称 y label
    ax2.set_title('Training Val Acc')  # 设置图名为Simple Plot
    ax2.legend()  # 自动检测要在图例中显示的元素，并且显示
    plt.savefig("val_acc.jpg")
    plt.show()  # 图形可视化

    # # TEST PRECISION
    fig3, ax3 = plt.subplots()  # 创建图实例

    ax3.plot(x, test_pres[0], label='test_acc_1')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax3.plot(x, test_pres[1], label='test_acc_2')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax3.plot(x, test_pres[2], label='test_acc_3')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax3.plot(x, test_pres[3], label='test_acc_4')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax3.plot(x, test_pres[4], label='test_acc_5')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax3.plot(x, test_pres[5], 'k', label='test_acc_clean')  # 作y2 = x^2 图，并标记此线名为quadratic

    ax3.set_xlabel('epochs')  # 设置x轴名称 x label
    ax3.set_ylabel('test_acc')  # 设置y轴名称 y label
    ax3.set_title('Training Test Acc')  # 设置图名为Simple Plot
    ax3.legend()  # 自动检测要在图例中显示的元素，并且显示
    plt.savefig("test_acc.jpg")
    plt.show()  # 图形可视化
