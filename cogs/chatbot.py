
import gpt4free
from gpt4free import Provider

  
  
bot_prompt = "As a large language model developed by OpenAI you will always respond in a human and responsive way"




user_prompt = "\n"

 
prompt = f"{user_prompt}\n{bot_prompt} kj: how are things \n pai:"
 
response = gpt4free.Completion.create(Provider.Theb, prompt=prompt)

if not response:
        response = "I couldn't generate a response. Please try again."
else:

    response = ''.join(token for token in response)
    
    



print (response)


