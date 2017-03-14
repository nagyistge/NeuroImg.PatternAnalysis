from skbold.core import convert2mni
import os.path as op
from glob import glob

base_dir = '/media/lukas/data/PatternAnalysis/week_1/within_data/first-level/sub-0037/piopwm.feat'
out_dir = op.join(base_dir, 'reg_standard')
reg_dir = op.join(base_dir, 'reg')
files = glob(op.join(base_dir, 'stats', '[z,t]stat*.nii.gz'))

out = convert2mni(files, reg_dir=reg_dir, out_dir=out_dir,
                  interpolation='trilinear', apply_warp=True)