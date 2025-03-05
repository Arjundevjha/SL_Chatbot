import openai
from config import Config

def get_chatbot_response(user_message, conversation_history=[]):
    """
    Get response from OpenAI API for the symposium chatbot
    """
    openai.api_key = Config.OPENAI_API_KEY
    
    messages = [
        {"role": "system", "content": Config.SYSTEM_PROMPT}
    ]
    
    # Add conversation history
    for msg in conversation_history[-5:]:  # Keep last 5 messages for context
        messages.append({"role": "user", "content": msg["user"]})
        if "assistant" in msg:
            messages.append({"role": "assistant", "content": msg["assistant"]})
    
    # Add current message
    messages.append({"role": "user", "content": user_message})
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message['content']
    except Exception as e:
        return "I apologize, but I'm having trouble responding right now. Please try again later."
