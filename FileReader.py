
import pandas as pd

#Creates the text object. It has the text/response and the ID.
class text:

    def __init__ (self, ID, fullText):
        self.ID = ID
        self.fullText = fullText

    def getID(self):
        return self.ID
    
    def getText(self):
        return self.fullText


#Reads the responses and creates an object with the ID and the text as a string.
def process_responses(csv_file_path):
    df = pd.read_csv(csv_file_path)
    responses = []
    for index, row in df.iterrows():
        ID = row['readingID']  #Gets ID from readingID column
        fullText = row['Response'] #Gets response from Response column
        response = text(ID, fullText)
        responses.append(response)
    return responses



#Reads the answer and creates 
def process_answers(csv_file_path):
    reference_df = pd.read_csv(csv_file_path)
    correct_answers = {}
    for index, row in reference_df.iterrows():
        ID = row['readingID']   #Gets ID from readingID column
        correct_text = row['Text']  #Gets text from Text column
        correct_answers[ID] = correct_text
    return correct_answers