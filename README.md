# Identification-Of-Users-with-Social-Behavioural-Biometrics-On-Twitter-Anudeep-G

Social behavioral biometrics in Twitter refers to the analysis of human behavior and interactions within the Twitter platform for the purpose of user identification and authentication. In this method, implementation for identifying Twitter users uses a combination of two feature extraction algorithms TF-IDF and Word2Vec to overcome the existing problem in TF-IDF. This combination generates important features from TF-IDF and these features are used to extract corresponding word vector from Word2vec algorithm. Then these feature vectors are utilized in classification algorithms (CNN, LSTM, CNN-LSTM) which undergoes multiple tensor layers to train and classify user identities. 

## Repository Contains 

1. /data - It contains a /Data folder (holds datasets of 4 users), Combining_datasets.py file (holds code to combine datasets to one csv file) and twitter_dataset.csv file (holds combined data of 4 users).
2. /src - It contains code files for 3 algorithms and pre-trained word2vec model.
3. /Block Diagrams - It contains flowchart of the project, block diagram of the code (functions and inputs) and block diagram for CNN, CNN-LSTM and LSTM Algorithms.


## Running the code:

1. Run Combining_datsets.py file in /data folder for generating all the twitter data into one csv file.
2. Update the path of the dataset file name in User_Identification_CNN-LSTM.ipynb, User_Identification_CNN.ipynb, User_Identification_LSTM.ipynb.
3. Run each file seperatly from src folder in jupyter lab or google colab.
