import React, { useState } from 'react';

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = () => {
    if (input.trim()) {
      setMessages([...messages, { text: input, id: messages.length }]);
      setInput('');
    }
  };

  return (
    <div className="chat">
      <h1>Chat with AI</h1>
      <div className="messages">
        {messages.map(message => (
          <div key={message.id} className="message">
            {message.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type your message..."
      />
      <button onClick={sendMessage}>Send</button>
      {/* Hier können weitere Funktionen wie das Teilen oder Speichern von Chats hinzugefügt werden */}
    </div>
  );
}

export default Chat;
