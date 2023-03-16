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

    txt_paths = [r'E:\pycharmproject\cleantest\runs4\log\大面指纹脏污_cleantest_200epochs_1.txt',
                 r'E:\pycharmproject\cleantest\runs4\log\大面指纹脏污_cleantest_200epochs_2.txt',
                 r'E:\pycharmproject\cleantest\runs4\log\大面指纹脏污_cleantest_200epochs_3.txt',
                 r'E:\pycharmproject\cleantest\runs4\log\大面指纹脏污_cleantest_200epochs_4.txt',
                 r'E:\pycharmproject\cleantest\runs4\log\大面指纹脏污_cleantest_200epochs_5.txt',
                 r'E:\pycharmproject\cleantest\runs4\log\大面指纹脏污_cleantest_200epochs_clean.txt']  # 将文件路径放在一个列表中
    train_losses, val_pres, test_pres = [], [], []
    for txt_path in txt_paths:
        train_loss, val_pre, test_pre = parse_txt(txt_path)
        train_losses.append(train_loss)
        val_pres.append(val_pre)
        test_pres.append(test_pre)
    print(train_losses, '\n', len(train_losses), len(train_losses[0]))
    print(val_pres, '\n', len(val_pres), len(val_pres[0]))
    print(test_pres, '\n', len(test_pres), len(test_pres[0]))
    fig, ax = plt.subplots()  # 创建图实例
    x = np.arange(1, len(test_pres[0])+1, 1)

    # # TRAIN LOSS
    # ax.plot(x, train_losses[0], label='train_loss_1')  # 作y1 = x 图，并标记此线名为linear
    # ax.plot(x, train_losses[1], label='train_loss_2')  # 作y1 = x 图，并标记此线名为linear
    # ax.plot(x, train_losses[2], label='train_loss_3')  # 作y1 = x 图，并标记此线名为linear
    # ax.plot(x, train_losses[3], label='train_loss_4')  # 作y1 = x 图，并标记此线名为linear
    # ax.plot(x, train_losses[4], label='train_loss_5')  # 作y1 = x 图，并标记此线名为linear
    # ax.plot(x, train_losses[5], 'k', label='train_loss_clean')  # 作y1 = x 图，并标记此线名为linear
    #
    # ax.set_xlabel('epochs')  # 设置x轴名称 x label
    # ax.set_ylabel('train_loss')  # 设置y轴名称 y label
    # ax.set_title('Training')  # 设置图名为Simple Plot
    # ax.legend()  # 自动检测要在图例中显示的元素，并且显示
    # plt.savefig("traing_loss.jpg")
    #
    # plt.show()  # 图形可视化

    # # VALID PRECISION
    # ax.plot(x, val_pres[0], label='val_acc_1')  # 作y2 = x^2 图，并标记此线名为quadratic
    # ax.plot(x, val_pres[1], label='val_acc_2')  # 作y2 = x^2 图，并标记此线名为quadratic
    # ax.plot(x, val_pres[2], label='val_acc_3')  # 作y2 = x^2 图，并标记此线名为quadratic
    # ax.plot(x, val_pres[3], label='val_acc_4')  # 作y2 = x^2 图，并标记此线名为quadratic
    # ax.plot(x, val_pres[4], label='val_acc_5')  # 作y2 = x^2 图，并标记此线名为quadratic
    # ax.plot(x, val_pres[5], 'k', label='val_acc_clean')  # 作y2 = x^2 图，并标记此线名为quadratic
    #
    # ax.set_xlabel('epochs')  # 设置x轴名称 x label
    # ax.set_ylabel('val_acc')  # 设置y轴名称 y label
    # ax.set_title('Training')  # 设置图名为Simple Plot
    # ax.legend()  # 自动检测要在图例中显示的元素，并且显示
    # plt.savefig("val_acc.jpg")
    # plt.show()  # 图形可视化

    # TEST PRECISION
    ax.plot(x, test_pres[0], label='test_acc_1')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax.plot(x, test_pres[1], label='test_acc_2')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax.plot(x, test_pres[2], label='test_acc_3')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax.plot(x, test_pres[3], label='test_acc_4')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax.plot(x, test_pres[4], label='test_acc_5')  # 作y2 = x^2 图，并标记此线名为quadratic
    ax.plot(x, test_pres[5], 'k', label='test_acc_clean')  # 作y2 = x^2 图，并标记此线名为quadratic

    ax.set_xlabel('epochs')  # 设置x轴名称 x label
    ax.set_ylabel('test_acc')  # 设置y轴名称 y label
    ax.set_title('Training')  # 设置图名为Simple Plot
    ax.legend()  # 自动检测要在图例中显示的元素，并且显示
    plt.savefig("test_acc.jpg")
    plt.show()  # 图形可视化
