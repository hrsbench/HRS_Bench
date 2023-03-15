import cv2
import os
import os.path
import sys
import numpy as np
import pandas as pd
import sys
import pickle


def detect_color_hue_based(hue_value):
    if hue_value < 15:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 39:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    else:
        color = "RED"

    return color


def load_gt(csv_pth):
    gt_data = pd.read_csv(csv_pth).to_dict('records')
    gt_list = []
    for sample in gt_data:
        # Objects:
        objs = [sample['obj1'], sample['obj2']]
        for i in range(3, 5):
            if type(sample['obj'+str(i)]) is str:  # check if there is an object
                objs.append(sample['obj'+str(i)])

        # Colors:
        colors = [sample['color1'], sample['color2']]
        for i in range(3, 5):
            if type(sample['color' + str(i)]) is str:  # check if there is other colors
                colors.append(sample['color' + str(i)])

        gt_list.append({"objs": objs, "colors": colors})

    return gt_list


def load_pred(pkl_pth, iter_idx):
    with open(pkl_pth, 'rb') as f:
        pred_data = pickle.load(f)

    pred_data = pred_data[iter_idx]
    pred_objs = {}
    for img_id, v in pred_data.items():
        temp_dict = {}
        for obj_id, v2 in v.items():
            item = v2[0]  # remove duplicate objects
            temp_dict[obj_id] = {"cls": item[-1]}
            # convert coordinates to float instead of str:
            cords = [float(cord) for cord in item[:4]]
            temp_dict[obj_id]["cords"] = cords  # (xmin, ymin, xmax, ymax)  # origin = top left

        pred_objs[img_id] = temp_dict

    return pred_objs


if __name__ == "__main__":
    in_pkl = sys.argv[1]
    gt_csv = sys.argv[2]
    # Load GT:
    gt_data = load_gt(csv_pth=gt_csv)
    iter_num = 1
    avg_acc = []
    acc_per_level = {0: [], 1: [], 2: []}
    for iter_idx in range(iter_num):
        for level in range(3):
            mul = int(len(gt_data) / 3)
            # Load Predictions:
            pred_data = load_pred(pkl_pth=in_pkl, iter_idx=iter_idx)
            # Calculate the counting Accuracy:
            acc = cal_acc(gt_data[level * mul:(level + 1) * mul], pred_data, level=level)
            avg_acc.append(acc)
            print("Accuracy ", iter_idx, ": ", acc, "%")
            # Per level:
            acc_per_level[level].append(acc)

    for level in range(3):
        print("----------------------------")
        if level == 0:
            print("   Easy level Results   ")
        elif level == 1:
            print("   Medium level Results   ")
        elif level == 2:
            print("   Hard level Results   ")
        print("precision: ", (sum(acc_per_level[level]) / len(acc_per_level[level])), "%")
    print("----------------------------")
    print("   Average level Results   ")
    print("Averaged Accuracy: ", (sum(avg_acc) / len(avg_acc)), "%")

    in_img = sys.argv[1]
    frame = cv2.imread(in_img)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    avg_hue = np.average(hsv_frame[:, :, 0])  # average hue component
    detected_color = detect_color_hue_based(avg_hue)
    print("Detected_color: ", detected_color)
