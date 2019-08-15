# 读取txt-标准txt为基准-分类别求阈值-阈值为0. 0.3 0.5 0.7的统计
import glob
import os
import numpy as np

# 设定的阈值
threshold1 = 0.3
threshold2 = 0.5
threshold3 = 0.7

# 阈值计数器
counter0 = 0
counter1 = 0
counter2 = 0
counter3 = 0

stdtxt = ''  # 标注txt路径
testtxt = ''  # 测试txt路径

txtlist = glob.glob(r'%s\*.txt' % stdtxt)  # 获取所有txt文件
for path in txtlist:  # 对每个txt操作

    txtname = os.path.basename(path)[:-4]  # 获取txt文件名
    label = 1
    eachtxt = np.loadtxt(path)  # 读取文件
    for line in eachtxt:
        line.insert(1)
        if line[0] == label:
            # 构建背景为0框为1的图
            map1 = np.zeros((960, 1280))
            map1[line[2]:(line[2] + line[4]), line[1]:(line[1] + line[3])] = 1

            testfile = np.loadtxt(testtxt + txtname + '.txt')
            c = 0
            iou_list = []  # 用来存储所有iou的集合
            for tline in testfile:  # 对测试txt的每行进行操作
                if tline[0] == label:
                    c = c + 1
                    map2 = np.zeros((960, 1280))
                    map2[tline[2]:(tline[2] + tline[4]), tline[1]:(tline[1] + tline[3])] = 1
                    map3 = map1 + map2
                    a = 0
                    for i in map3:
                        if i == 2:
                            a = a + 1
                    iou = a / (line[3] * line[4] + tline[3] * tline[4] - a)  # 计算iou
                    iou_list.append(iou)  # 添加到集合尾部

            threshold = max(iou_list)  # 阈值取最大的
            # 阈值统计
            if threshold >= threshold3:
                counter3 = counter3 + 1
            elif threshold >= threshold2:
                counter2 = counter2 + 1
            elif threshold >= threshold1:
                counter1 = counter1 + 1
            elif threshold < threshold1:  # 漏检
                counter0 = counter0 + 1
if __name__ == '__main__':
    print(counter0, counter1, counter2, counter3)
