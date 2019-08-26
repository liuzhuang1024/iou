import numpy as np
import cv2
import os
import tqdm
import glob

yuzhi = 0.7


def iou(box1, box2):
    '''
    两个框（二维）的 iou 计算

    注意：边框以左上为原点

    box:[top, left, bottom, right]
    '''
    in_h = min(box1[4], box2[4]) - max(box1[0], box2[0])
    in_w = min(box1[5], box2[5]) - max(box1[1], box2[1])
    inter = 0 if in_h < 0 or in_w < 0 else in_h * in_w
    union = (box1[4] - box1[0]) * (box1[5] - box1[1]) + \
            (box2[4] - box2[0]) * (box2[5] - box2[1]) - inter
    iou = inter / union
    return iou


def get_iou(file1, file2):
    # box1 = gt
    box1 = np.loadtxt(file1, dtype=float, delimiter=',')
    box2 = np.loadtxt(file2, dtype=float, delimiter=',')
    count = 0
    for i in box1:
        for j in box2:
            if iou(i, j) > yuzhi:
                count += 1
                break
    miou = count / len(box1)
    if miou <= 1:
        return miou
    else:
        return 1


def get_score(dir1, dir2):
    # dir1 = gt
    l1 = glob.glob(os.path.join(dir1, '*.txt'))
    l2 = glob.glob(os.path.join(dir2, '*.txt'))
    name = []
    score = []
    for i in tqdm.tqdm(l1):
        j = os.path.join(dir2, os.path.basename(i))
        if j in l2:
            name.append(name)
            score.append(get_iou(i, j))
    avg = np.average(np.array(score))
    print(avg)
    return avg


if __name__ == '__main__':
    get_score('gt', 'test')
