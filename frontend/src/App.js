import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState('');

    const sendMessage = async () => {
        try {
            const res = await axios.post('http://127.0.0.1:5000/api/chat', { message });
            setResponse(res.data.reply);
        } catch (error) {
            console.error(error);
            setResponse("Error communicating with backend.");
        }
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>Chatbot App</h1>
            <textarea
                placeholder="Type your message here..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                style={{ width: '100%', height: '100px', marginBottom: '10px' }}
            ></textarea>
            <br />
            <button onClick={sendMessage}>Send</button>
            <div>
                <h3>Response:</h3>
                <p>{response}</p>
            </div>
        </div>
    );
};

export default App;
