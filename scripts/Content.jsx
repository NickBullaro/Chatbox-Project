    
import * as React from 'react';


import { Button } from './Button';
import { Socket } from './Socket';

export function Content() {
    const [users, setUsers] = React.useState([]);
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
            Socket.on('new user', updateUsers);
            return () => {
                Socket.off('new user', updateUsers);
            }
        });
    }
    
    function updateMessages(data) {
        console.log("Received messages from server: " + data['allMessages']);
        setMessages(data['allMessages']);
        let chatBox = document.getElementById("box");
        chatBox.scrollTop = chatBox.scrollHeight;
    }
    
    function updateUsers(connected) {
        console.log('Received new sid: ' + connected['allUsers']);
        setUsers(connected['allUsers']);
    }
    
    getNewuser();
    getNewMessage();


    
    return (
        <div class="chatbox">
            <h1>Messages!</h1>
                <ul id="box">
                    {
                        messages.map((message, index) =>
                        <li key={index}>Name : {message}</li>)
                    }
                </ul>
            <Button />
        </div>
    );
}
