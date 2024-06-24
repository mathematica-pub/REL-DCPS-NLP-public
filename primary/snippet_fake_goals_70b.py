## Imports
import os
from generate_text import generate_text 
import pandas as pd  
   
## Prepare models
model1 = "./model/Meta-Llama-3-8B-Instruct-Q8_0.gguf" 
model2 = "./model/Meta-Llama-3-70B-Instruct-Q4_K_S.gguf" 

## Prepare Goals for analysis
# - Load the data from the Excel file
input_path = "./data/fake_goals.csv"
goal_data = pd.read_csv(input_path)
goal_data.info()
# - Preliminary cleaning
keep_cols = ["goal_id", "goal"]
cln_data = goal_data.dropna(
    subset=["goal"]
    ).loc[
    :, keep_cols
    ]  
 
## Step by step prompting (small model)
system_prompt = """
You give feedback on the quality of the goals teachers set for their students. 
Treat all submitted text as a goal. 
First, give feedback on the quality of the goal for each of these categories: specificity, measurability, achievability, and deadline clarity.
Second, give advice on how to improve the goal. 
Finally, give a score from 1 (needs improvement) to 5 (excellent) for each category. 
"""  
check_small = generate_text(cln_data.goal.tolist(),
                 system_prompt = system_prompt, 
                 model_path = model1,
                 temperature = 0.0, 
                 n_ctx = 1024, max_tokens = 1024)  



[print("________\n", check_small['prompts'][i], "\n", check_small['responses'][i]) \
    for i in range(len(check_small['responses']))]
print(check_small)

## Big model
check_big = generate_text(cln_data.goal.tolist(),
                 system_prompt = system_prompt, 
                 model_path = model2,
                 temperature = 0.0, 
                 n_ctx = 1024, max_tokens = 1024)  



[print("________\n", check_big['prompts'][i], "\n", check_big['responses'][i]) \
    for i in range(len(check_big['responses']))]
print(check_big )

## Step by step prompting with equity (Big model)
system_prompt = """
You give feedback on the quality of the goals teachers set for their students. 
Treat all submitted text as a goal. 
First, give feedback on the quality of the goal for each of these categories: specificity, measurability, achievability, deadline clarity, as well as equity and inclusivity.
Second, give advice on how to improve the goal. 
Finally, give a score from 1 (needs improvement) to 5 (excellent) for each category. 
"""  
check_big_ie = generate_text(cln_data.goal.tolist(),
                 system_prompt = system_prompt, 
                 model_path = model2,
                 temperature = 0.0, 
                 n_ctx = 1024, max_tokens = 1024)  



[print("________\n", check_big_ie['prompts'][i], "\n", check_big_ie['responses'][i]) \
    for i in range(len(check_big_ie['responses']))]
print(check_big_ie) 

## Export responses
outdata = cln_data.copy(deep=True)

outdata['check_big_ie'] = check_big_ie['responses']
outdata['check_big']    = check_big['responses']
outdata['check_small']  = check_small['responses']
outdata.to_csv("./data/fake_goal_feedback.csv", index = False)