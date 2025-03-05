from flask import Flask, render_template, request, session
from config import Config
from utils.chat_helper import get_chatbot_response
from data.symposium_info import SCHEDULE, WORKSHOPS, SHOWCASE, SPEAKER_INFO

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def chat():
    if 'conversation' not in session:
        session['conversation'] = []
    
    response = None
    if request.method == 'POST':
        user_message = request.form.get('message', '').strip()
        if user_message:
            # Get chatbot response
            response = get_chatbot_response(user_message, session['conversation'])
            
            # Update conversation history
            session['conversation'].append({
                "user": user_message,
                "assistant": response
            })
            session.modified = True
    
    return render_template('chat.html', 
                         conversation=session['conversation'],
                         schedule=SCHEDULE,
                         workshops=WORKSHOPS,
                         showcase=SHOWCASE,
                         speaker_info=SPEAKER_INFO)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
