# Identification-Of-Users-with-Social-Behavioural-Biometrics-On-Twitter-Anudeep-G

Social behavioral biometrics in Twitter refers to the analysis of human behavior and interactions within the Twitter platform for the purpose of user identification and authentication. This code repository contains the implementation for identifying Twitter users using a combination of two feature extraction algorithms TF-IDF and Word2Vec to overcome the existing problem which only uses TF-IDF. This combination generates important features from TF-IDF and these features are used to extract coressponding word vector from Word2vec algorithm. Then these feature vectors are utilized in classification algorithms (CNN, LSTM, CNN-LSTM) which undergoes multiple tesnsor layers to train and classify user identities. 

## Repository Contains 

1. /data - It contains datasets of 4 twitter users. Total Samples: 88,209
2. /src - It contains code files for 3 algorithms and pre-trained word2vec model which is generated while implemnting the code.
