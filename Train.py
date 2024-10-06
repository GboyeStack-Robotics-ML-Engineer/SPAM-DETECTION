from torch.utils.data import Dataset,DataLoader
import lightning as L
import pandas as pd
import torch
import DataGenerator
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import prepare_data_module
from prepare_data_module import DataModule

class TRAINNER(L.LightningModule):

    def __init__(self,model):
        super().__init__()
        self.model=model
        self.outputs=None
        self.loss=None
    
    
    def forward(self, input_ids,attention_mask, labels=None):
        #device='cuda' if torch.cuda.is_available() else 'cpu'
                
        B,_,S=input_ids.shape
        
        input_ids=input_ids.view(B,S)
        
        attention_mask=attention_mask.view(B,S)

        BT,_,ST=labels.shape
        
        labels=labels.view(BT,ST).type(torch.LongTensor)
        
        self.outputs=self.model(
                                input_ids=input_ids,
                                attention_mask=attention_mask,
                                labels=labels
                                )
        self.loss=self.outputs.loss
        
        
        return self.loss
    
    def training_step(self,batch,batch_idx):

        input_ids=batch['input']
        
        attention_mask=batch['attention_mask']
        
        labels=batch['labels']
        
        self.model.train()
        
        train_loss=self.forward(input_ids=input_ids,attention_mask=attention_mask,labels=labels)
        
        self.log('Train_Loss',train_loss,prog_bar=True,logger=True)
    
    
    def validation_step(self,batch,batch_idx):
        
        input_ids=batch['input']
        
        attention_mask=batch['attention_mask']
        
        labels=batch['labels']
        
        self.model.eval()
        
        val_loss=self.forward(input_ids=input_ids,attention_mask=attention_mask,labels=labels)
        
        self.log('Val_Loss',val_loss,prog_bar=True,logger=True)
        
    def test_step(self,batch,batch_idx):
        
        input_ids=batch['input']
        
        attention_mask=batch['attention_mask']
        
        labels=batch['labels']
        
        test_loss=self.forward(input_ids=input_ids,attention_mask=attention_mask,labels=labels)
        
        self.log('test_Loss',test_loss,prog_bar=True,logger=True)
    
    def configure_optimizers(self):
        
        optimizer = torch.optim.Adam(self.model.parameters(), lr=1e-3)
        lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=1)

        return [optimizer], [lr_scheduler]
    
    def save(self):
        
        self.model.save_pretrained()


from transformers import T5ForConditionalGeneration,T5Tokenizer
MODEL_NAME='t5-base'
model=T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
tokenizer=T5Tokenizer.from_pretrained(MODEL_NAME)

data=pd.read_csv(r"C:\Users\Admin\OneDrive\Desktop\ManaGPT-1020_4080_prompts_and_generated_texts.csv")
train_data=data.copy().sample(frac=0.8)
test_data=data.copy().sample(frac=0.2)
valid=data.copy().sample(frac=0.4)

data_module=DataModule(train=train_data,
            test=test_data,
            valid=valid,
            tokenizer=tokenizer,
            batch_size=2)

data_module.setup()

trainer=L.Trainer(
    max_epochs=100,
    enable_progress_bar=True,
    num_sanity_val_steps=0,
    logger=None,
    callbacks=None
)

classifier=TRAINNER(model=model)
trainer.fit(classifier,datamodule=data_module)


    
    