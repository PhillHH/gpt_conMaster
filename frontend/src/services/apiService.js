// src/services/apiService.js
import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000'; // Stelle sicher, dass dies mit deinem Backend übereinstimmt

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const createChat = async (message) => {
  const response = await api.post('/chats', { message });
  return response.data;
};

export const getChats = async () => {
  const response = await api.get('/chats');
  return response.data;
};

export const getChat = async (chatId) => {
  const response = await api.get(`/chats/${chatId}`);
  return response.data;
};

export const updateChat = async (chatId, message) => {
  const response = await api.put(`/chats/${chatId}`, { message });
  return response.data;
};

export const deleteChat = async (chatId) => {
  const response = await api.delete(`/chats/${chatId}`);
  return response.data;
};

export const createBranch = async (chatId, message, parentId = null) => {
  const response = await api.post('/branches/create', { chat_id: chatId, message, parent_id: parentId });
  return response.data;
};

export const getBranch = async (branchId) => {
  const response = await api.get(`/branches/${branchId}`);
  return response.data;
};
