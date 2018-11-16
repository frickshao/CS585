from textgenrnn import textgenrnn
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

textgen=textgenrnn('iheartmindy_twitter_weights.hdf5')
textgen.generate_samples()
