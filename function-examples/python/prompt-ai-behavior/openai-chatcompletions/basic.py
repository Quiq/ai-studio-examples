# Pass the last customer message straight to the LLM (no conversation history)
# and pass the LLM completion straight back to the customer as text. This 
# example assumes use within a customer assistant 

def build_basic(llm, context):
  content = context['derivedData']['lastCustomerMessage'] 
  return {
    "request": {
      "messages": [{"role": "user", "content": content}]
    }
  }

def handle_basic(llm, context, prompt, response, completion):
  return { "actions": [
    {
      "action": "sendMessage",
      "message": {"text": completion}
    }
  ]}

