import React, { useState } from 'react';
import axios from 'axios';
import ContentBox from '../components/ContentBox';
import './chatPage.css';

const ChatPage = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');

    const sendMessage = async () => {
        if (!input.trim()) return;

        const newMessage = { role: 'user', content: input };
        setMessages([...messages, newMessage]);

        try {
            const response = await axios.post('http://localhost:5000/chat', {
                message: input,
            });

            const reply = response.data.reply;
            setMessages([...messages, newMessage, { role: 'assistant', content: reply }]);
            setInput('');
        } catch (error) {
            console.error('Error sending message:', error);
        }
    };

    return (
        <ContentBox>
            <div className="chat-container">
                <div className="chat-history">
                    {messages.map((msg, index) => (
                        <div key={index} className={`message ${msg.role}`}>
                            <span>{msg.content}</span>
                        </div>
                    ))}
                </div>
                <div className="chat-input">
                    <input
                        id="chat-input"
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        placeholder="How can i help you today..."
                    />
                    <button onClick={sendMessage}>Send</button>
                </div>
            </div>
        </ContentBox>
    );
};

export default ChatPage;
