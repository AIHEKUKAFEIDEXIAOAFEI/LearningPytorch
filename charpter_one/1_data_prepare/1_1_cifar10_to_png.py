"""

"""

from scipy.misc import imsave
import numpy as np
import os
import pickle



data_dir = os.path.join("..", "..", "Data", "cifar-10-batches-py")

train_o_dir = os.path.join("..", "..", "Data", "cifar-10-png", "raw_train")

test_o_dir = os.path.join("..", "..", "Data", "cifar-10-png", "raw_test")

Train = False # only unzip test set

# unzip , and return dict of unzipped info
def unpickle(file):
	with open(file, 'rb') as fo:
		dict_ = pickle.load(fo, encoding='bytes')
	return dict_

def my_mkdir(my_dir):
	if not os.path.isdir(my_dir):
		os.makedirs(my_dir)

# generate train images
if __name__ == '__main__':
	if Train:
		for j in range(1,6):
			data_path = os.path.join(data_dir,"data_batch_" + str(j)) # data_batch_1,2,3,4,5
			train_data = unpickle(data_path)
			print(data_path + "is loading...")
			
			for i in range(0, 10000):
				img = np.reshape(train_data[b'data'], (3,32,32))
				img = img.transpose(1,2,0)
				
				label_num = str(train_data[b'labels'][i])
				o_dir = os.path.join(train_o_dir, label_num)
				my_mkdir(o_dir)

				img_name = label_num + '_' + str(i + (j - i)*10000) + '.png'
				img_path = os.path.join(o_dir, img_name)
				imsave(img_path, img)
			print(data_path + " loaded.")
	
	print("test_batch is loading...")

	# generate test images
	test_data_path = os.path.join(data_dir, "test_batch")
	test_data = unpickle(test_data_path)
	for i in range(0, 10000):
		img = np.reshape(test_data[b'data'][i], (3,32,32))
		img = img.transpose(1, 2, 0)
		
		label_num = str(test_data[b'labels'][i])	
		o_dir = os.path.join(test_o_dir, label_num)
		my_mkdir(o_dir)

		img_name = label_num + '_' + str(i) + '.png'
		img_path = os.path.join(o_dir, img_name)
		imsave(img_path, img)
	
	print("test_batch loaded...")
