import os.path as op
from glob import glob
from skbold.core import MvpWithin

base_dir = '/media/lukas/data/PatternAnalysis/final_project/SharedStatesData'
feats = glob(op.join(base_dir, 'sub*', '*.feat'))
mask = '/media/lukas/data/Software/skbold/skbold/data/ROIs/other/GrayMatter_prob.nii.gz'

for feat in feats:

    mvp = MvpWithin(source=feat, read_labels=True, remove_contrast=['Cue'],
                    ref_space='epi', beta2tstat=True, remove_zeros=True,
                    mask=mask, mask_threshold=25)
    mvp.create()
    mvp.write(op.dirname(feat))
