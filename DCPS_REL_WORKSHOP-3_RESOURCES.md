# Structure of this Document

- Discussion of potential important tools
    - Post-processing
    - OpenAI on Azure
- Discussion of additional more advanced LLM topics
    - Prompt Engineering
    - RAG (Retrieval Augmented Generation)
    - Fine-tuning

# Potential key tools
## Post-Processing

We now have long text output based on our prompts and goals. However, to make use of this text, we need to convert it into a usable format. 

A classic approach is to extract the numbers for each category using regular expressions. Since the OpenAI output was most consistant in it's format, we can write a quick function to extract the scores in python. You could easily do a similar extraction/cleaning step in R or stata if those are preferred for analysis. 

Our example is in `snippet_postprocess_responses.py`. Additionally, [this](https://learnbyexample.github.io/python-regex-cheatsheet/) helpful guide gives a comprehensive description of regular expressions in python and many examples, and [this](https://regex101.com/) website is very helpful for debugging regular expressions. 
## OpenAI on Azure

OpenAI has a partnership with Azure such that OpenAI models can be run securely, without transferring any information to OpenAI. 

This guide walks you through the process (focus on the OpenAI Python 1.X approach)

This requires filling out the application [here](https://customervoice.microsoft.com/Pages/ResponsePage.aspx?id=v4j5cvGGr0GRqy180BHbR7en2Ais5pxKtso_Pz4b1_xUNTZBNzRKNlVQSFhZMU9aV09EVzYxWFdORCQlQCN0PWcu). 

Then one needs to set up an OpenAI resource in Azure, most likely a Gpt3.5Turbo resource. From there, using the secure OpenAI models in Azure closely resembles using the general OpenAI API. A guide from Microsoft on using the Azure OpenAI service is [here](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart?tabs=command-line%2Cpython-new&pivots=programming-language-python), and an example of python code to use the OpenAI Azure approach is available on the OpenAI Github [here](https://github.com/openai/openai-python?tab=readme-ov-file#microsoft-azure-openai).

Many of the key resources available in the general OpenAI API can be used securely in Azure, but not all of them. The availability and costs for OpenAI services on Azure are described [here](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/).   

The OpenAI example from the examples we shared will help introduce you to this approach, but will not work "out of the box". 

# Additional more advanced LLM topics
There are 3 key potential ways to increase the context and usefulness of LLMs, and they all relate to making the outputs more aligned with your interests. 

The first is prompt engineering, where you manipulate the form or content of the prompt. You can inject context by querying a database and adding the info directly. 

The second is RAG, which manipulates the content and form of the prompt by using the prompt to query an auxiliary database and injecting the result into the final prompt or the output. This process, in contrast to prompt engineering, allows for uncertainty in what exact information might be deemed most relevant for a particular prompt because RAG is choosing the context to add based on the prompt submitted. 

The third is fine tuning, which allows you to train the models themselves to emulate particular prompt-response pairs you submit. This option changes the model itself, which is it's strength and it's weakness. It is also expensive and more restricted to particular tasks. Prompt engineering and RAG are often better to consider first. 
## Prompt Engineering

While fine-tuning can help with certain tasks, there are some risks associated with it and if possible it would be better to use prompt engineering or RAG (to be discussed later) as these will scale better if you switch to a different model provider or want to slightly alter the form of the desired output. 

A wide variety of prompt engineering guides exist. [Here](https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results) is OpenAI's guide, [here](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview#prompting-vs-finetuning) is anthropic's, and [here](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering) is Microsoft's. Additionally, [this paper](https://arxiv.org/html/2402.05201v1#S2) describes 5 common prompt engineering approaches. 

Even more complex prompt engineering approaches could allow us to embed context directly from the dataset into our prompts. To do this, we could edit our generate_text function to include another input beyond just `{user_input}`. Thus, we can use certain information and query against auxiliary data to, for example, for a student ID, get the age, expectations, subject area, school system, etc. and add those. 

An example might be to add `{grade_level}` to the prompt, so that the prompt template "human" section would read 

``` 
("human", "Grade: " + {grade_level} + ". Goal: " + {user_input}" + prompt_end)
``` 


Additionally, it is sometimes helpful to use LLMs to generate prompts. I made a very simple example of such a prompt-engineering conversation [here](https://chatgpt.com/share/9fb5f7d1-2b48-4ed0-8ad9-18b987f1fb43) in line with this example. Anthropic has a (paid) service specifically designed to help with prompt engineering, described [here](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator). 


## Retrieval Augmented Generation


Retrieval Augmented Generation (RAG) takes this idea further, and uses the input prompt to query against a database of additional information and then embeds the most relevant queried information into the prompt. 

It can also encourage the response to rely on the database for answers. 

[This](https://towardsdatascience.com/retrieval-augmented-generation-rag-from-theory-to-langchain-implementation-4e9bd5f6a4f2) blog post gives a good brief overview. 
## Fine Tuning

Fine tuning is an additional option for improving LLM output. 

This allows you to train the models themselves to emulate particular prompt-response pairs you submit. This option changes the model itself, which is it's strength and it's weakness. 

Its strength is that the model is not being encouraged to accomplish your task, it is forced to by aligning it's outputs with your examples. 

Its weakness is that the alignment with the examples can lead to "catastrophic forgetting" where the model can no longer handle other contexts.

Another weakness is the cost: fine tuning requires training a model, not just using it, and model training is computationally taxing. It also won't translate to a new model, and you would have to re-fine tune another model if you changed approaches. 

For this reason, prompt engineering and RAG are often better to consider first. 

Some guides on fine tuning are from OpenAI [here](https://platform.openai.com/docs/guides/fine-tuning/when-to-use-fine-tuning) and from Microsoft [here](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/fine-tuning?tabs=turbo%2Cpython-new&pivots=programming-language-studio). 



