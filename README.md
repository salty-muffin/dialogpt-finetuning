# gpt-2-training

for dataset parsing, dataset preperation & finetuning gpt-2 to generate conversations about ai, cybernetics, control and ghosts

### directions

1. parse `.eml` mails with `mail_parsing/parse_editing.py`
2. manually add turn them into a chat like:
   - person1> message text.
   - person2> message text.
   - ...
3. finetune gpt-2/neo model with the chat using the notebook `aitextgen_finetune.ipynb`

## research links

- [dialoGPT finetuning](https://towardsdatascience.com/make-your-own-rick-sanchez-bot-with-transformers-and-dialogpt-fine-tuning-f85e6d1f4e30)
- [hugginface model database](https://huggingface.co/models)
- [hugginface transformer docs](https://huggingface.co/transformers/)

### setup

1. to create the envorinment: `conda env create -f environment.yml` or `conda env create -f environment-cpu.yml` for a cpu only version
2. activate the enviroment: `conda activate transformers`
