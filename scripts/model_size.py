import os
import re
import tqdm
import pickle
import pandas as pd

def find_file(path, file_name):
    sha_pd = pd.DataFrame(columns = ['modelname', 'lfs_file', 'lfs_sha', 'lfs_size'])
    total = 0
    sha_dict = {}
    for file_dir in tqdm.tqdm(os.listdir(path)):
        for file in os.listdir(os.path.join(path, file_dir)):
            if re.match(file_name, file):
                # get the content of the file
                try:
                    f_open = open(os.path.join(path, file_dir, file))
                    f_content = f_open.readlines()
                    f_content = [i.strip() for i in f_content]
                    sha = f_content[1].split(':')[1]
                    model_name = file_dir.replace(' ', '/')
                    size = f_content[2].split()[1]
                    sha_dict[model_name] = sha
                    sha_pd.loc[len(sha_pd)] = [model_name, file, sha, size]
                    break
                except:
                    print(model_name)
                    break
        total += 1
    print(sha_pd)
    return total, sha_dict, sha_pd


if __name__ == '__main__':
    total, sha_dict, sha_pd = find_file('../../hf_models_repos/', '.*\.bin$')
    # pickle.dump(sha_pd, open('sha_pd.pkl', 'wb'))
    # # pickle dump
    # pickle.dump(sha_dict, open('sha_dict.pkl', 'wb'))

    # pickle.dump(sha_dict, open('sha_dict.pkl', 'rb'))
    print('total_number', total)
    print('total_sha', len(sha_dict))
    print('distinct_sha', len(set(list(sha_dict.values()))))
