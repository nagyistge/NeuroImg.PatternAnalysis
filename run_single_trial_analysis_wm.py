from skbold.exp_model import FsfCrawler
import os.path as op

base_dir = '/media/lukas/data/PatternAnalysis/week_1/within_data'
preproc_dir = op.join(base_dir, 'preproc')
run_idf = 'piopwm'
template = 'mvpa'
output_dir = op.join(base_dir, 'first-level')
subject_idf = 'sub'
func_idf = 'func'
prewhiten = True
derivs = False
n_cores = 1

fsfc= FsfCrawler(preproc_dir, run_idf, template='mvpa',
                 output_dir=output_dir, subject_idf='sub',
                 func_idf='func', prewhiten=True, derivs=False,
                 n_cores=1)

fsfc.crawl()
