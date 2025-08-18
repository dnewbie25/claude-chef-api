import anthropic
import os
from dotenv import load_dotenv
load_dotenv()
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

SYSTEM_PROMPT = """
You are an assistant that receives a list of ingredients that a user has and suggests a recipe they could make with some or all of those ingredients.
You don't need to use every ingredient they mention in your recipe.
The recipe can include additional ingredients they didn't mention, but try not to include too many extra ingredients.
Format your response in markdown to make it easier to render to a web page.
"""

ingredientsList = ["tomatoe","carrot","beef","onion"]
def chef_claude(ingredients_list):
  message = client.messages.create(
      model="claude-sonnet-4-20250514",
      max_tokens=1000,
      temperature= 1,
      system= SYSTEM_PROMPT,
      messages=[
          {
              "role": "user",
              "content": [{
                "type":"text",
                "text":f"I have {', '.join(ingredients_list)}. Please give me a recipe you'd recommend I make!"
              }]
          }
      ]
  )
  return message.content