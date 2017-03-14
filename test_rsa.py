import os.path as op
from glob import glob
import joblib as jl
import numpy as np
from scipy.ndimage import imread
from scipy.spatial.distance import pdist


def argsort(seq):
    return sorted(range(len(seq)), key=seq.__getitem__)


base_dir = '/media/lukas/data/PatternAnalysis/final_project/SharedStatesData'
img_paths = glob(op.join(base_dir, 'images', '*.jpg'))

mvps = sorted(glob(op.join(base_dir, 'sub*', '*.jl')))

for mvp in mvps[0:1]:
    print(mvp)
    seq = op.join(glob(op.join(op.dirname(mvp), '*.feat'))[0], 'stim_sequence.txt')
    seq = np.loadtxt(seq, dtype=str)
    idx = argsort(seq)
    print(sorted(seq))
    sorted_p = [img_paths for (idx, img_paths) in sorted(zip(idx, img_paths))]

    print(sorted_p)
    imgs = [imread(img) for img in img_paths]
    imgs_rgb = np.stack([img.mean(axis=(0, 1)) for img in imgs])
    img_rsa = 1 - pdist(imgs_rgb, metric='correlation')
