## Imports
from typing import List
import pandas as pd
import os 

from openai import OpenAI
import openai
  
## Set API key
### Replace 'your-api-key' with your actual OpenAI API key
your_api_key = ''
assert your_api_key != '' , "Please set your OpenAI API key"

client = OpenAI(api_key=your_api_key)
 
## Define text feedback function

def get_openai_response(messages: List) -> str:
    """
    Get response from OpenAI model.

    Args: 
        messages (List): List of messages in Open AI input format.
    """

    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages,
      temperature=0.0,
      max_tokens=1024,
      top_p=1
    )
    return response.choices[0].message.content
 
## Set prompt
system_prompt = """
You give feedback on the quality of the goals teachers set for their students. 
Treat all submitted text as a goal. 
First, give feedback on the quality of the goal for each of these categories: specificity, measurability, achievability, deadline clarity, as well as equity and inclusivity.
Second, give advice on how to improve the goal. 
Finally, give a score from 1 (needs improvement) to 5 (excellent) for each category. 
"""  

## Set goals (based on the same fake goals data)
fake_goals = pd.read_csv("./data/fake_goal_feedback.csv")

## Create list of messages from fake goals in Open AI input format
messages_list = [
    [{"role": "system", "content": system_prompt}, 
     {"role": "user", "content": fg}]
    for fg in fake_goals["goal"]
  ]
print(fake_goals["goal"])

## Get responses
responses = [get_openai_response(messages) for messages in messages_list]
[print(r) for r in responses]

fake_goals["openai_responses"] = responses

## Save the responses to a csv file
fake_goals.to_csv("./data/fake_goal_feedback_w_openai.csv", index=False)