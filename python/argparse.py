# """
# 测试学习下参数载入
# """
# import argparse
# # 参数解析
#
# parser = argparse.ArgumentParser(description='你猜我要干啥')
#
# # type是要传入的参数的数据类型  help是该参数的提示信息
# parser.add_argument('--par1', type=str, default='苹果', help='你最爱的水果')
# parser.add_argument('--par2', type=str, required=True, help='你最爱的人')
# args = parser.parse_args()
#
# # 获得传入的参数
# print(f'{args.par1}并不是{args.par2}')
