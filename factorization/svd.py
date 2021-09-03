import argparse

from surprise import SVD, Dataset

from preprocess.data_iterator import read_data


def svd_trainer(data: Dataset):
  svd = SVD()
  svd.fit(data)
  return svd


def svd_predictor(svd: SVD, uid, iid):
  return svd.predict(uid, iid)


def parse_argument():
  parser = argparse.ArgumentParser()
  parser.add_argument('--path',
                      default='../data/movielens/ratings_small.csv')

  args = parser.parse_args()
  return args


def main():
  args = parse_argument()
  data = read_data(args.path)
  svd = svd_trainer(data)
  print(svd_predictor(svd, 1, 302))
  return


if __name__ == '__main__':
  main()
