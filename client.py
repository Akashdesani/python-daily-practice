from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)