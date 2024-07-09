from openai import OpenAI

# pip install openai 

client = OpenAI(
  api_key="your-api-key-here",  # Write your API key here
)

command = '''
anything for testing
'''

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named HADI who speaks Urdu as well as English. You are from Pakistan and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
    {"role": "user", "content": command},
  ]
)


print(completion.choices[0].message["content"])