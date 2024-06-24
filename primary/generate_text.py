## Imports
import os
import time

from typing import List

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import LlamaCpp 


## Define text feedback function
def generate_text(input_prompts : List[str],
                 system_prompt: str = "You are a helpful assistant.", 
                 model_path: str = "./model/Meta-Llama-3-8B-Instruct-Q3_K_S.gguf" ,
                 temperature: float = 0.3, 
                 n_ctx: int = 512, 
                 max_tokens: int = 256) -> dict: 
    """
    Generate text using a LlamaCpp model. 

    Args: 
        input_prompts (List[str]): List of prompts to generate text for.
        system_prompt (str): System prompt for the model.
        model_path (str): Path to the model file.
        temperature (float): Sampling temperature for model output.
        n_ctx (int): Number of tokens in the context window.
        max_tokens (int): Maximum tokens to generate in a single call.
    """

    ## Ensure model path exists
    assert os.path.exists(model_path)
    
    ## set batch size
    n_batch = n_ctx // 4
                   
    ## Instruct
    # Load the LlamaCpp language model, adjust GPU usage based on your hardware
    llm = LlamaCpp(
        # Path to model
        model_path=model_path,
        # Number of tokens in the context window
        n_ctx=n_ctx, 
        # Batch size for model processing
        n_batch=n_batch,   
        # Maximum tokens to generate in a single call
        max_tokens=max_tokens, 
        # Sampling temperature for model output 
        temperature=temperature, 
        # Tokens to indicate when to stop generating
        stop=["<|eot_id|>",  "assistant\n\n"] 
        )

    # Define the prompt template with a placeholder for the question
    prompt_end = "<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{user_input}" + prompt_end),
        ])   

    # Create an LLMChain to manage interactions with the prompt and model
    chain = template | llm 

    # Invoke the chain
    batch_prompts = [{"user_input": p} for p in input_prompts]

    start = time.time()
    responses = chain.batch(batch_prompts)
    end = time.time()
    
    elapsed = end - start

    # Return output
    output = {"system_prompt": system_prompt,
              "prompts": input_prompts, 
              "responses": responses, 
              "elapsed": elapsed}
    return output
