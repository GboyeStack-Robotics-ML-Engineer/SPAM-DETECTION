
def generate(model,tokenizer,content):
    
    encoded_content=tokenizer(content, padding='longest', return_tensors="pt",add_special_tokens=True)
    
    output=model.generate(**encoded_content)
    
    decoded_content=tokenizer.batch_decode(output,skip_special_tokens=True)
    
    return " ".join(decoded_content)
    
    
