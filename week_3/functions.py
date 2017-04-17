import numpy as np
import pandas as pd

def make_conceptual_rdm(y):
    rdm = np.vstack([y != y_tmp for y_tmp in y])
    return rdm.astype(int)

def kendalltau_a(a, b):
    
    n = a.size
    K = 0
    for k in range(n - 1):
        pairrel_a=np.sign(a[k]-a[k+1:n])
        pairrel_b=np.sign(b[k]-b[k+1:n])
        K += np.sum(pairrel_a * pairrel_b)
    return K/(n*(n-1) / 2.0)

def extract_contrast_names(design_file):
    
    contrasts = np.sum([1 if 'ContrastName' in line else 0
                        for line in open(design_file)])

    n_lines = np.sum([1 for line in open(design_file)])

    df = pd.read_csv(design_file, delimiter='\t', header=None,
                     skipfooter=n_lines - contrasts, engine='python')

    cope_labels = list(df[1].str.strip())  # remove spaces
    cope_labels = ["_".join(c.split('_')[:-1]) if c.split('_')[-1].isdigit()
                   else c for c in cope_labels]
    return cope_labels

