import pandas as pd
from surprise import Reader, Dataset
from surprise.model_selection import KFold

def read_data(path):
  df = pd.read_csv(path)
  data = Dataset.load_from_df(df[['userId', 'movieId', 'rating']], reader=Reader())
  kf = KFold(n_splits=5)
  kf.split(data)
  train = data.build_full_trainset()
  return train