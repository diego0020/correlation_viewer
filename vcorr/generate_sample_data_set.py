__author__ = 'Diego'


import numpy as np
import pandas as pd


def generate_sample_data(n_vars,n_subjs):
    subjects = ["subj_%d"%i for i in xrange(n_subjs)]
    df = pd.DataFrame(index=subjects)
    for var in xrange(n_vars):
        array = np.random.random(len(subjects))
        df["var_%d"%var] = array
    return df

if __name__ == "__main__":
    import os
    file_name = os.path.join(os.path.dirname(__file__),"..","test_data.csv")
    test_df = generate_sample_data(20,40)
    test_df.to_csv(file_name)
