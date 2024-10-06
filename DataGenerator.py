from torch.utils.data import Dataset
import torch 

class Generator(Dataset):

    def __init__(self, dataset=None,tokenizer=None,max_length=None):

        self.dataset= dataset
        
        self.tokenizer=tokenizer
        
        self.max_length=max_length


    def __len__(self):
        
        return self.dataset.shape[0]

    
    def __getitem__(self, idx):
        
        assert type(idx)==int, f'Expected {int} got type {idx}'

        data= self.dataset.iloc[idx,:]
        
        message,id= data[0],data[1]
    
        class_id=torch.zeros(2)
        
        class_id=class_id.index_fill(dim=-1,index=torch.tensor(id,dtype=torch.int64),value=torch.tensor(1))
        
        input_text_tokens = self.tokenizer(message, padding='max_length', return_tensors="pt",add_special_tokens=False,max_length=self.max_length)
        
        sample={'input':input_text_tokens['input_ids'],
                'attention_mask':input_text_tokens['attention_mask'],
                'label':class_id}
        return sample
