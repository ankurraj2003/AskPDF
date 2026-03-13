css = '''
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

body {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: radial-gradient(circle at top right, #1e293b, #0f172a);
}

[data-testid="stSidebar"] {
    background-color: rgba(15, 23, 42, 0.8) !important;
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

/* Glowing divider */
hr {
    border: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, #3b82f6, transparent);
    margin: 2rem 0;
}

.chat-message {
    padding: 1.5rem; 
    border-radius: 1.2rem; 
    margin-bottom: 1.5rem; 
    display: flex;
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px) scale(0.98); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}

.chat-message:hover {
    transform: translateY(-4px) scale(1.01);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.chat-message.user {
    background: rgba(59, 130, 246, 0.12);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2);
    border-right: 4px solid #3b82f6;
    flex-direction: row-reverse;
}

.chat-message.user:hover {
    box-shadow: 0 0 25px rgba(59, 130, 246, 0.4);
}

.chat-message.bot {
    background: rgba(139, 92, 246, 0.08);
    box-shadow: 0 8px 32px 0 rgba(139, 92, 246, 0.15);
    border-left: 4px solid #8b5cf6;
}

.chat-message.bot:hover {
    box-shadow: 0 0 25px rgba(139, 92, 246, 0.4);
}

.chat-message .avatar {
    width: 65px;
    height: 65px;
    flex-shrink: 0;
}

.chat-message .avatar img {
    width: 65px;
    height: 65px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid rgba(255, 255, 255, 0.3);
    padding: 2px;
    background: rgba(255, 255, 255, 0.1);
}

.chat-message .message {
    flex-grow: 1;
    padding: 0 2rem;
    color: #f1f5f9;
    line-height: 1.7;
    font-size: 1.05rem;
    text-shadow: 0 1px 2px rgba(0,0,0,0.2);
}

.chat-message.user .message {
    text-align: right;
}

h1, h2, h3 {
    background: linear-gradient(to right, #fff, #94a3b8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700 !important;
}

.stButton>button {
    background: linear-gradient(90deg, #2563eb 0%, #7c3aed 100%);
    color: white;
    border: none;
    padding: 0.75rem 2rem;
    border-radius: 0.75rem;
    font-weight: 600;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    width: 100%;
    border: 1px solid rgba(255, 255, 255, 0.1);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 20px rgba(59, 130, 246, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.3);
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/337/337946.png" alt="Bot">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Felix&backgroundColor=b6e3f4" alt="User">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
