from torch.utils.data import Dataset
import torch 
import warnings

class Generator(Dataset):

    def __init__(self, dataset=None,tokenizer=None,max_length=None,padding_style='max_length'):

        self.dataset= dataset
        
        self.tokenizer=tokenizer
        
        self.max_length=max_length

        self.padding_style=padding_style

    def __len__(self):
        
        return self.dataset.shape[0]

    
    def __getitem__(self, idx):
        
        assert type(idx)==int, f'Expected {int} got type {idx}'

        default_padding_length=min(1024,self.tokenizer.max_len_single_sentence)

        if self.padding_style is None:

          self.padding_style='max_length'
          
          self.max_length=default_padding_length
        
        else:

          if self.padding_style=='max_length' and self.max_length is None:

            warnings.warn(f'Padding was set to {self.padding_style} and the max_length was set to None. A default max length of min(1024,tokenizer.max_len_single_sentence). To overide this set the max length  when you specify the padding style as {self.padding_style}')

            self.max_length=default_padding_length


        dataset_columns=self.dataset.columns.tolist()[1:]
        message,id_= self.dataset[dataset_columns[0]].values.tolist()[idx],self.dataset[dataset_columns[1]].values.tolist()[idx]
        
        class_id=torch.zeros(2)
        
        class_id=class_id.index_fill(dim=-1,index=torch.tensor(id_,dtype=torch.int64),value=torch.tensor(1))
        
        input_text_tokens = self.tokenizer(message, padding=self.padding_style, return_tensors="pt",add_special_tokens=False,max_length=self.max_length,truncation=True)
        
        sample={'input':input_text_tokens['input_ids'],
                'attention_mask':input_text_tokens['attention_mask'],
                'label':class_id}
        return sample
