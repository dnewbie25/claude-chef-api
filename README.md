# Claude Chef API

This API provides AI-powered recipe suggestions based on a list of ingredients you provide. It uses Anthropic's Claude model to generate creative and useful recipes, formatted in markdown for easy web rendering.

## Features

- Accepts a list of ingredients and returns a recipe suggestion.
- Powered by Anthropic Claude for high-quality, context-aware responses.
- CORS enabled for local and web development.
- Runs on a dedicated server for reliability and performance.

## POST /recipe

- **Endpoint:** `/recipe`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "ingredients": ["tomato", "carrot", "beef", "onion"]
  }
  ```
- **Response:**
- Returns a markdown-formatted recipe suggestion using some or all of the provided ingredients.

## Running

The API is deployed and running on a dedicated server. You can interact with it from your frontend or API client.

---

**Note:** You must provide a valid Anthropic API key in the `.env` file for the service to function.
