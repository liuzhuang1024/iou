def iou(box1, box2):
    '''
    两个框（二维）的 iou 计算

    注意：边框以左上为原点

    box:[top, left, bottom, right]
    '''
    in_h = min(box1[2], box2[2]) - max(box1[0], box2[0])
    in_w = min(box1[3], box2[3]) - max(box1[1], box2[1])
    inter = 0 if in_h < 0 or in_w < 0 else in_h * in_w
    union = (box1[2] - box1[0]) * (box1[3] - box1[1]) + \
            (box2[2] - box2[0]) * (box2[3] - box2[1]) - inter
    iou = inter / union
    return iou


if __name__ == '__main__':
    print(iou([2, 2, 5, 5, ], [2, 2, 4, 4, ]))
