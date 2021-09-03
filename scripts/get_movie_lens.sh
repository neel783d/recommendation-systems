#!/bin/bash
# please setup kaggle api credentials
# Credit: https://www.kaggle.com/rounakbanik/the-movies-dataset

mkdir -p data
kaggle datasets download -d rounakbanik/the-movies-dataset -p data/
unzip data/the-movies-dataset.zip -d data/movielens/
rm data/the-movies-dataset.zip