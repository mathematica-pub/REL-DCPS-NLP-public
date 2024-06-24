# REL-DCPS-NLP
Repository for DCPS session on using NLP to improve analysis of goals

1. Download the GGUF Meta-Llama-3-8B quantized model from [here](https://huggingface.co/bartowski/Meta-Llama-3-8B-Instruct-GGUF).

On your local Windows machine, you should probably stick with something like the `Q3_K_M` model [here](https://huggingface.co/bartowski/Meta-Llama-3-8B-Instruct-GGUF/blob/main/Meta-Llama-3-8B-Instruct-Q4_K_M.gguf). 

> **NOTE:** Files bigger than 4.30 GB are hard to run on Windows

2. Using powershell, create a `conda` environment using the provided `environment.yml` file (this may take >15 minutes):
```
$ conda env create -f environment.yml
$ conda activate DCPS-NLP
```
