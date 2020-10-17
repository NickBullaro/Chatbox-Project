import * as React from 'react';

import { Button } from './Button';
import { Socket } from './Socket';

export function Content() {
    const [users, setUsers] = React.useState('');
    const [messages, setMessages] = React.useState([]);
    
    function getNewMessage() {
        React.useEffect(() => {
            Socket.on('messages received', updateMessages);
            return () => {
                Socket.off('messages received', updateMessages);
            }
        });
    }
    
    function getNewuser() {
        React.useEffect(() => {
            Socket.on('users received', updateUsers);
            return () => {
                Socket.off('users received', updateUsers);
            }
        });
    }
    
    function updateMessages(data) {
        console.log("Received messages from server: " + data['allMessages']);
        setMessages(data['allMessages']);
        let chatBox = document.getElementById("box");
        chatBox.scrollTop = chatBox.scrollHeight;
    }
    
    function updateUsers(data) {
        console.log('Received new sid: ' + data['all_users']);
        setUsers(data['all_users']);
    }
    
    getNewuser();
    getNewMessage();


    
    return (
        <div className="chatbox">
            <h1>Messages!</h1>
                <ul id="box">
                    {
                        messages.map((message, index) =>
                        <li key={index}>{message}</li>)
                    }
                </ul>
            <Button />
            <h2 className="users">Total users: {users}</h2>
        </div>
    );
}