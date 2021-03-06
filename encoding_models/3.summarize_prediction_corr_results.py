import numpy,scipy.stats

import os,glob,pickle

predacc_files=glob.glob('../models/encoding/*/predacc*')

predacc_files_noshuf=[i for i in predacc_files if not i.find('shuf')>-1]
results={'shuf':{},'noshuf':{}}
for p in predacc_files_noshuf:
    model=os.path.dirname(p).split('/')[-1]
    p=pickle.load(open(p,'rb'))
    results['noshuf'][model]={'len':len(p),'mean':numpy.mean([x[2] for x in p])}
print(results['noshuf'])
predacc_files_shuf=[i for i in predacc_files if i.find('shuf')>-1]
for i,p in enumerate(predacc_files_shuf):
    print('loading %d/%d'%(i,len(predacc_files_shuf)))
    model=os.path.dirname(p).split('/')[-1]
    p=pickle.load(open(p,'rb'))
    if not model in results['shuf']:
        results['shuf'][model]=[]
    results['shuf'][model].append(numpy.mean([x[2] for x in p]))
    print(results['shuf'][model][-1])
pickle.dump(results,open('predacc_results.pkl','wb'))
for model in results['shuf'].keys():
    print(model,results['noshuf'][model],scipy.stats.scoreatpercentile(results['shuf'][model],95))
