// Create the FAB container
const fab = document.createElement('button');
fab.id = 'material-fab';
fab.className = 'material-fab';
fab.innerHTML = '<span class="material-fab-icon">&#43;</span>'; // Plus icon

// Create the chat window
const chatWindow = document.createElement('div');
chatWindow.id = 'material-chat-window';
chatWindow.className = 'material-chat-window';

// Chat window content (simple header and input)
chatInput = document.createElement('input');
chatInput.id = 'chat-input';
chatInput.type = 'text';
chatInput.placeholder = 'Ask LLM...';
chatInput.className = 'material-chat-input';

chatMessages = document.createElement('div');
chatMessages.id = 'chat-messages';
chatMessages.className = 'material-chat-messages';

chatWindow.appendChild(chatMessages);
chatWindow.appendChild(chatInput);

// Handle chat input submit
function submitChatMessage() {
  const input = chatWindow.querySelector('#chat-input');
  const messages = chatWindow.querySelector('#chat-messages');
  const text = input.value.trim();
  if (text) {
    const msg = document.createElement('div');
    msg.className = 'material-chat-message material-chat-message-send';
    msg.textContent = text;
    messages.appendChild(msg);
    input.value = '';
    messages.scrollTop = messages.scrollHeight;

    const reply = document.createElement('div');
    reply.className = 'material-chat-message material-chat-message-receive';
    messages.appendChild(reply);
    messages.scrollTop = messages.scrollHeight;
    reply.textContent = "...";

    // Placeholder
    setTimeout(() => {
      reply.textContent = `Your mum ${text}`;
    }, Math.floor(Math.random() * 10 + 1) * 1000); // Simulate 2 second API response delay

  }
}

// Listen for Enter key in input
chatWindow.addEventListener('keydown', (e) => {
  if (e.target.id === 'chat-input' && e.key === 'Enter') {
    submitChatMessage();
  }
});

// Show chat window when FAB is clicked
fab.addEventListener('click', () => {
  if (chatWindow.style.display === 'flex') {
    chatWindow.style.display = 'none';
    fab.innerHTML = '<span class="material-fab-icon">&#43;</span>';
  } else {
    chatWindow.style.display = 'flex';
    fab.innerHTML = '<span class="material-fab-icon">&times;</span>';
    chatInput.focus();
  }
});

// Add to DOM when script loads
window.addEventListener('DOMContentLoaded', () => {
  document.body.appendChild(fab);
  document.body.appendChild(chatWindow);
});
