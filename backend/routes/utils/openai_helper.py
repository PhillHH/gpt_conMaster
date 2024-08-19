import openai
from flask import current_app

def query_openai_api(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=current_app.config.get('OPENAI_TEMPERATURE', 0.7),
            max_tokens=current_app.config.get('OPENAI_MAX_TOKENS', 150),
            top_p=current_app.config.get('OPENAI_TOP_P', 1.0),
            frequency_penalty=current_app.config.get('OPENAI_FREQUENCY_PENALTY', 0.0)
        )
        return response['choices'][0]['message']['content']
    except openai.error.OpenAIError as e:
        current_app.logger.error(f"OpenAI API error: {e}")
        return "There was an issue with the OpenAI API."
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {e}")
        return "An unexpected error occurred."