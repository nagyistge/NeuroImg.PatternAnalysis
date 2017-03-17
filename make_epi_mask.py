from skbold.core import convert2epi
import os.path as op

base_dir = '/media/lukas/data/PatternAnalysis/week_1/'
mask = op.join(base_dir, 'Left_Amygdala_mask.nii.gz')
reg_dir = op.join(base_dir, 'sub-0037_workingmemory_WITHIN.feat', 'reg')

convert2epi(mask, reg_dir=reg_dir)
