import torch
from transformers import AutoTokenizer, GPT2LMHeadModel
tokenizer = AutoTokenizer.from_pretrained("gpt2")
# add the EOS token as PAD token to avoid warnings
model = GPT2LMHeadModel.from_pretrained("gpt2", pad_token_id = tokenizer.eos_token_id)

torch.manual_seed(42)

model_inputs = tokenizer.encode('I enjoy walking with my cute dog', return_tensors = 'pt')

greedy_output = model.generate(model_inputs, max_length = 500, num_beams = 5, no_repeat_ngram_size = 2, num_return_sequences = 5)


print("My GPT-2 Story:")
print("---------------")
print(tokenizer.decode(greedy_output[0], skip_special_tokens = True))