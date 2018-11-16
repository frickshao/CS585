from textgenrnn import textgenrnn

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#use this code to create a new model based on the supplied text document
#textgen = textgenrnn()
#textgen.train_from_file('tweets.txt', num_epochs = 5)

#use this code to generate output based on the models created from above
textgen_2 = textgenrnn('textgenrnn_weights.hdf5')
textgen_2.generate(10, temperature = .9)
