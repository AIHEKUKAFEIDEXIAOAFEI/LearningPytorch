"""
	split the original data into train set, val set and test set
"""

import os
import glob
import random
import shutil


dataset_dir = os.path.join("..", "..", "Data", "cifar-10-png", "raw_test")
train_dir = os.path.join("..", "..", "Data", "train")
valid_dir = os.path.join("..", "..", "Data", "valid")
test_dir = os.path.join("..", "..", "Data", "test")

train_per = 0.8
valid_per = 0.1
test_per = 0.1
