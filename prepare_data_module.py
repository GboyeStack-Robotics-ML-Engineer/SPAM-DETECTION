import DataGenerator
from DataGenerator import Generator
import torch 
import lightning as L
import transformers
from torch.utils.data import Dataset,DataLoader


class DataModule(L.LightningDataModule):
    
    def __init__(self,train,test,valid,batch_size,tokenizer,max_length=None,padding_style=None):
        super().__init__()
        self.train_data=train
        self.test_data=test
        self.validation_data=valid
        self.batch_size=batch_size
        self.tokenizer=tokenizer
        self.max_length=max_length
        self.padding_style=padding_style

    def setup(self,stage=None):
        pass
    def prepare_data(self):
        
        self.train_data_=Generator(dataset=self.train_data,tokenizer=self.tokenizer,max_length=self.max_length,padding_style=self.padding_style)
        self.test_data_=Generator(dataset=self.test_data,tokenizer=self.tokenizer,max_length=self.max_length,padding_style=self.padding_style)
        self.validation_data_=Generator(dataset=self.validation_data,tokenizer=self.tokenizer,max_length=self.max_length,padding_style=self.padding_style)
                    
    def train_dataloader(self):
     
        return DataLoader(self.train_data_,batch_size=self.batch_size,shuffle=True,num_workers=2,persistent_workers=True)
    
    def test_dataloader(self):
        
        return DataLoader(self.test_data_,batch_size=self.batch_size,shuffle=True,num_workers=2,persistent_workers=True)
    
    def val_dataloader(self):
        
        return DataLoader(self.validation_data_,batch_size=self.batch_size ,shuffle=True,num_workers=2,persistent_workers=True)