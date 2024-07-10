# REL-DCPS-NLP
Repository for DCPS session on using NLP to improve analysis of goals

0. Download this repository using git

If neccesary, install git [here](https://git-scm.com/download/win). Then, in the folder you'd like to store the code and models, run the command `git clone https://github.com/mathematica-pub/REL-DCPS-NLP-public.git` using git bash (open git bash by right-clicking empty space in windows explorer and clicking "Open Git Bash here" in the menu that appears).  

1. Download the GGUF Meta-Llama-3-8B quantized model from [here](https://huggingface.co/bartowski/Meta-Llama-3-8B-Instruct-GGUF).

On your local Windows machine, you should probably stick with something like the `Q3_K_M` model [here](https://huggingface.co/bartowski/Meta-Llama-3-8B-Instruct-GGUF/blob/main/Meta-Llama-3-8B-Instruct-Q4_K_M.gguf). 

> **NOTE:** Files bigger than 4.30 GB are hard to run on Windows

2. Install anaconda

3. Using powershell, create a `conda` environment using the provided `environment.yml` file (this may take >15 minutes):
```
$ conda env create -f environment.yml
$ conda activate DCPS-NLP
```

4. In anaconda navigator, select the DCPS-NLP environment and open Jupyter

5. Use a Jupyter notebook to explore the commands in the `.py` files in this repository. 

