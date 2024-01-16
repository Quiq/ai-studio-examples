# Pass the last customer message straight to the LLM (no conversation history)
# and pass the LLM completion straight back to the customer as text. This 
# example assumes use within a customer assistant 

def build_basic(llm, context):
  last_cust_message = context['derivedData']['lastCustomerMessage'] 

  return {
    "request": {
      "prompt": last_cust_message,
      "max_tokens_to_sample": 256
    }
  }

def handle_basic(llm, context, prompt, response, completion):
  return { "actions": [
    {
      "action": "sendMessage",
      "message": {"text": completion}
    }
  ]}

