// src/components/ChatList.js
import React, { useEffect, useState } from 'react';
import { getChats } from '../services/apiService';

const ChatList = () => {
  const [chats, setChats] = useState([]);

  useEffect(() => {
    const fetchChats = async () => {
      const data = await getChats();
      setChats(data);
    };
    fetchChats();
  }, []);

  return (
    <div>
      <h2>Chat List</h2>
      <ul>
        {chats.map((chat) => (
          <li key={chat.id}>{chat.message}</li>
        ))}
      </ul>
    </div>
  );
};

export default ChatList;
