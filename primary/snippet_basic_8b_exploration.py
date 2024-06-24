## Imports
import os 
from generate_text import generate_text

## Set up model paths
### We want to compare the responses from models with different quantization sizes 
 
## Generate responses for basic prompts
model1 = "./model/Meta-Llama-3-8B-Instruct-Q3_K_S.gguf" 
basic_prompts = ["Tell me a joke", "Explain the big bang in simple terms"]
system_prompt = "You are a helpful assistant."
basic_small = generate_text(basic_prompts,
                 system_prompt = system_prompt, 
                 model_path = model1,
                 temperature = 0.3, 
                 n_ctx = 128, max_tokens = 256 )  

print(basic_small)
[print(p) for p in basic_small["responses"]] 

## Now try a bigger model
model2 = "./model/Meta-Llama-3-8B-Instruct-Q4_K_M.gguf"
basic_large = generate_text(basic_prompts,
                 system_prompt = system_prompt, 
                 model_path = model2,
                 temperature = 0.3, 
                 n_ctx = 128, max_tokens = 256 ) 

print(basic_large)
[print(p) for p in basic_large["responses"]]

## Now try a different prompt
system_prompt_pirate = "You are a helpful assistant who talks like a pirate."
basic_large_pirate = generate_text(basic_prompts,
                 system_prompt = system_prompt_pirate, 
                 model_path = model2,
                 temperature = 0.3, 
                 n_ctx = 128, max_tokens = 256 ) 

print(basic_large_pirate)
[print(p) for p in basic_large_pirate["responses"]].
 
## Using the bigger model
model3 = "./model/Meta-Llama-3-8B-Instruct-Q8_0.gguf" 
basic_gigantic_pirate = generate_text(basic_prompts,
                 system_prompt = system_prompt_pirate, 
                 model_path = model3,
                 temperature = 0.3, 
                 n_ctx = 128, max_tokens = 256 ) 
 
print(basic_gigantic_pirate) 
[print(p) for p in basic_gigantic_pirate["responses"]]
 
## Try a more complex prompt, referencing likert scale and survey responses
likert = "You are an assistant. Use the 5 point likert scale " + \
         "(strongly disagree, disagree, neutral, agree, strongly agree) " + \
         "to indicate whether you think the survey respondent is physically old " + \
         "based on their response to \"do you consider yourself young or an old?\""

survey_responses = [
    "Survey response: I don't relate with either possible answer. " + \
    "Instead, I find myself oscillating between the two frequently.",

    "Survey response: I like to think of myself as young at heart. " + \
    "Even though I'm old in years, I love adventure and learning."]     

likert_large = generate_text(survey_responses,
                 system_prompt = likert, 
                 model_path = model2,
                 temperature = 0.3, 
                 n_ctx = 256, max_tokens = 256 ) 
print(likert_large) 
[print(p) for p in likert_large['responses']]

## Using the bigger model
likert_gigantic = generate_text(survey_responses,
                 system_prompt = likert,
                 model_path = model3,
                 temperature = 0.3, 
                 n_ctx = 256, max_tokens = 256 ) 
print(likert_gigantic)
[print(p) for p in likert_gigantic['responses']]
  