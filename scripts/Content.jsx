    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';

export function Content() {
    const [messages, setMessages] = React.useState([]);
    
    function getNewMessage() {
        React.useEffect(() => {
            Socket.on('messages received', updateMessages);
            return () => {
                Socket.off('messages received', updateMessages);
            }
        });
    }
    
    function updateMessages(data) {
        console.log("Received messages from server: " + data['allMessages']);
        setMessages(data['allMessages']);
    }
    
    getNewMessage();

    return (
        <div class="chatbox">
            <h1>Messages!</h1>
                <ul>
                    {
                        messages.map((message, index) =>
                        <li key={index}>Name: {message}</li>)
                    }
                </ul>
            <Button />
        </div>
    );
}
