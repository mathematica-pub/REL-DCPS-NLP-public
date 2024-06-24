## Imports
import os
from generate_text import generate_text 
import pandas as pd  

## Prepare models
model = "./model/Meta-Llama-3-8B-Instruct-Q8_0.gguf"  

## Prepare School data for analysis
# - Load the data from the Excel file
data_directory = "Your Path/"
input_path = data_directory + "Intervention Sample_lbNotes.csv"
goal_data = pd.read_csv(input_path)
goal_data.info()
# - Preliminary cleaning
keep_cols = ["intervention_id", "subject_area", "grade_level", "school_id"
             , "group_intervention_name", "strategies", "strategy_ids", "tier"
             , "in_group", "plan_goal"]
cln_data = goal_data.dropna(
    subset=["plan_goal"]
    ).loc[
    :, keep_cols
    ]

print(cln_data.groupby(['grade_level', "subject_area"]).intervention_id.count())
print(cln_data.loc[cln_data.grade_level=="6"].groupby(['subject_area']).intervention_id.count())
print(cln_data.loc[cln_data.grade_level=="11"].groupby(['subject_area']).intervention_id.count())
print(cln_data.loc[cln_data.grade_level=="C7"].groupby(['subject_area']).intervention_id.count())

## Confirm intervention_id is unique
cln_data.intervention_id.nunique() == cln_data.shape[0]

math_prompts = cln_data.loc[
    (cln_data.grade_level=="6") & (cln_data.subject_area=="Mathematics")
    ].sample(
    3
    ).loc[
    :, ["intervention_id", "plan_goal"]
    ] 
behave_prompts = cln_data.loc[
    (cln_data.grade_level=="6") & (cln_data.subject_area=="Behavior")
    ].sample(
    3
    ).loc[
    :, ["intervention_id", "plan_goal"]
    ]
    

## Simple "Smart" feedback
system_prompt = """
You give feedback on the quality of the goals teachers set for their students. 
Treat all submitted text as a goal. 
Goals should be specific, measurable, achievable, and have a deadline.
Give feedback on the extent to which goals are specific, measurable, achievable, or have a deadline.
Include a numeric score for each category from 1 (needs improvement) to 5 (excellent). 
"""  
math_simple = generate_text(math_prompts.plan_goal.tolist(),
                 system_prompt = system_prompt, 
                 model_path = model,
                 temperature = 0.0, 
                 n_ctx = 1024, max_tokens = 1024)  



[print("________\n", math_simple['prompts'][i], "\n", math_simple['responses'][i]) \
    for i in range(len(math_simple['responses']))]
print(math_simple)
    
behave_simple = generate_text(behave_prompts.plan_goal.tolist(),
                 system_prompt = system_prompt, 
                 model_path = model,
                 temperature = 0.0, 
                 n_ctx = 1024, max_tokens = 1024)  

 
[print("________\n", behave_simple['prompts'][i], "\n", behave_simple['responses'][i]) \
    for i in range(len(behave_simple['responses']))]
print(behave_simple)
      
## Step by step prompting
system_prompt = """
You give feedback on the quality of the goals teachers set for their students. 
Treat all submitted text as a goal. 
First, give feedback on the quality of the goal for each of these categories: specificity, measurability, achievability, and deadline clarity.
Second, give advice on how to improve the goal. 
Finally, give a score from 1 (needs improvement) to 5 (excellent) for each category. 
"""  
math_step = generate_text(math_prompts.plan_goal.tolist(),
                 system_prompt = system_prompt, 
                 model_path = model,
                 temperature = 0.0, 
                 n_ctx = 1024, max_tokens = 1024)  



[print("________\n", math_step['prompts'][i], "\n", math_step['responses'][i]) \
    for i in range(len(math_step['responses']))]
print(math_step)
    
behave_step = generate_text(behave_prompts.plan_goal.tolist(),
                 system_prompt = system_prompt, 
                 model_path = model,
                 temperature = 0.0, 
                 n_ctx = 1024, max_tokens = 1024)  

 
[print("________\n", behave_step['prompts'][i], "\n", behave_step['responses'][i]) \
    for i in range(len(behave_step['responses']))]
print(behave_step)
    
## Step by step prompting (equity/inclusion)
system_prompt = """
You give feedback on the quality of the goals teachers set for their students. 
Treat all submitted text as a goal. 
First, give feedback on the quality of the goal for each of these categories: specificity, measurability, achievability, deadline clarity, as well as equity and inclusivity.
Second, give advice on how to improve the goal. 
Finally, give a score from 1 (needs improvement) to 5 (excellent) for each category. 
"""  
math_step_ie = generate_text(math_prompts.plan_goal.tolist(),
                 system_prompt = system_prompt, 
                 model_path = model,
                 temperature = 0.0, 
                 n_ctx = 1024, max_tokens = 1024)  



[print("________\n", math_step_ie['prompts'][i], "\n", math_step_ie['responses'][i]) \
    for i in range(len(math_step_ie['responses']))]
print(math_step_ie)
    
behave_step_ie = generate_text(behave_prompts.plan_goal.tolist(),
                 system_prompt = system_prompt, 
                 model_path = model,
                 temperature = 0.0, 
                 n_ctx = 1024, max_tokens = 1024)  

 
[print("________\n", behave_step_ie['prompts'][i], "\n", behave_step_ie['responses'][i]) \
    for i in range(len(behave_step_ie['responses']))]
print(behave_step_ie)

## add output data to the goal_data
math_prompts["simple_feedback"] = math_simple['responses']
math_prompts["step_feedback"] = math_step['responses']
math_prompts["step_ie_feedback"] = math_step_ie['responses']

behave_prompts["simple_feedback"] = behave_simple['responses']
behave_prompts["step_feedback"] = behave_step['responses']
behave_prompts["step_ie_feedback"] = behave_step_ie['responses']

## Save the data 
math_prompts.to_csv(data_directory + "math_prompts.csv", index=False)
behave_prompts.to_csv(data_directory + "behave_prompts.csv", index=False)