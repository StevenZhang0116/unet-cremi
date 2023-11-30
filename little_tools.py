import os
import re

data_dir = os.path.join(".","plain")
train_dir = os.path.join(data_dir, "train")
val_dir = os.path.join(data_dir, "val")
train_fns = os.listdir(train_dir)
val_fns = os.listdir(val_dir)


def extract_integers(s):
    return [int(num) for num in re.findall(r'\d+', s)]

def check_index(search_lst):
    intlst = []
    for i in search_lst:
        if i != ".DS_Store":
            intlst.append(extract_integers(i)[0])
    unique_lst = list(set(intlst))
    unique_lst.sort()
    return unique_lst

train_int = check_index(train_fns)
val_int = check_index(val_fns)

ll = len(train_int)

for i in range(ll):
    backbone_raw = "_raw.jpeg"
    backbone_rawindex = "_raw.npy"
    backbone_cleft = "_cleft.jpeg"
    backbone_cleftindex = "_cleft.npy"
    backbone_neuron = "_neuron.jpeg"
    backbone_neuronindex = "_neuron.npy"

    backbonelist = [backbone_raw, backbone_rawindex, backbone_cleft, backbone_cleftindex, backbone_neuron, backbone_neuronindex]

    for j in backbonelist:
        os.rename(f"{train_dir}/{train_int[i]}{j}", f"{train_dir}/{i}{j}")
        print(f"Rename to: {train_dir}/{i}{j}")