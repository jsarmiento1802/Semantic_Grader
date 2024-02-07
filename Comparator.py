from sentence_transformers import SentenceTransformer, util
from FileReader import process_responses, process_answers
import pandas as pd

print("funciona!")

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

responses = process_responses(r"File path for responses")
answers = process_answers(r"File Path for answers")


# Read existing Excel file
excel_file_path = r"File path for Graded file"
df = pd.read_excel(excel_file_path)

# Iterate through responses and calculate scores
scores = []
for response in responses:
    response_id = response.getID()
    response_text = response.getText()
    
    if response_text and not pd.isna(response_text) and response_id in answers:
        correct_answer_text = answers[response_id]
        
        if not response_text.strip():
            score = 0
        else:
            # Calculate similarity score
            response_embedding = model.encode(response_text, convert_to_tensor=True)
            answer_embedding = model.encode(correct_answer_text, convert_to_tensor=True)
            similarity_score = util.pytorch_cos_sim(response_embedding, answer_embedding)
            score = similarity_score.item()
    else:
        score = 0
        
    scores.append(score)

# Add scores to a new column called "Grade" in the DataFrame
df['Grade'] = scores

# Save the modified DataFrame back to the Excel file
df.to_excel(excel_file_path, index=False)

