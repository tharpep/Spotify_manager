from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "Your are the bean man, you like beans a lot. And music."},
    {"role": "user", "content": "What is your favorite song? You have to pick one song."}
  ]
)

print(completion.choices[0].message)