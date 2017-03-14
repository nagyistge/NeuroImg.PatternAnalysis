import os.path as op
import pandas as pd
import numpy as np
from glob import glob

base_dir = '/media/lukas/data/PatternAnalysis/final_project/SharedStatesData'
logs = glob(op.join(base_dir, 'sub*', '*.feat', '*.log'))

for log in logs:

    df = pd.read_csv(log, sep='\t', skiprows=3)['Code']
    codes = [x for x in df if str(x).isdigit() and len(str(x)) == 3]
    codes = sorted(codes, key=lambda x: x[0])
    img_ids = ['0' + x[1:] + '.jpg' for x in codes]
    np.savetxt(op.join(op.dirname(log), 'stim_sequence.txt'), img_ids, fmt='%s')
