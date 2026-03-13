css = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

body {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
}

[data-testid="stSidebar"] {
    background-color: rgba(30, 41, 59, 0.7);
    backdrop-filter: blur(10px);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

.chat-message {
    padding: 1.5rem; 
    border-radius: 1rem; 
    margin-bottom: 1.5rem; 
    display: flex;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    animation: fadeIn 0.5s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}

.chat-message:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
}

.chat-message.user {
    background: rgba(59, 130, 246, 0.15);
    border-left: 4px solid #3b82f6;
    flex-direction: row-reverse;
}

.chat-message.bot {
    background: rgba(255, 255, 255, 0.05);
    border-left: 4px solid #8b5cf6;
}

.chat-message .avatar {
    width: 60px;
    height: 60px;
    flex-shrink: 0;
}

.chat-message .avatar img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid rgba(255, 255, 255, 0.2);
}

.chat-message .message {
    flex-grow: 1;
    padding: 0 1.5rem;
    color: #e2e8f0;
    line-height: 1.6;
    font-size: 1rem;
}

.chat-message.user .message {
    text-align: right;
}

h1, h2, h3 {
    color: #f8fafc !important;
    font-weight: 600 !important;
}

.stButton>button {
    background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%);
    color: white;
    border: none;
    padding: 0.5rem 2rem;
    border-radius: 0.5rem;
    font-weight: 600;
    transition: all 0.3s ease;
    width: 100%;
}

.stButton>button:hover {
    transform: scale(1.02);
    box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://api.dicebear.com/7.x/bottts/svg?seed=Felix&backgroundColor=b6e3f4" alt="Bot">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Aneka&backgroundColor=ffdfbf" alt="User">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''