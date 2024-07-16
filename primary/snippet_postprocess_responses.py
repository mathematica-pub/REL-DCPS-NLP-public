## Imports
import pandas as pd
import os  
import re
  
## Read in goals
fake_goals = pd.read_csv("./data/fake_goal_feedback_w_openai.csv")

## Look at examples of openai responses
fake_goals.openai_responses[0]
fake_goals.openai_responses[1]

### We see that each dimension has a single digit score at the end

## Extract those scores with regular expressions
### Loop through dimensions and extract the digits

outcome_dims = ['Specificity', 'Measurability', 'Achievability', 'Deadline clarity', 'Equity and inclusivity']

for dim in outcome_dims:
    fake_goals[dim] = fake_goals['openai_responses'].str.extract(dim + r': (\d)', expand=False)

## Save the data

fake_goals.to_csv("./data/fake_goal_feedback_w_openai_scores.csv", index=False)