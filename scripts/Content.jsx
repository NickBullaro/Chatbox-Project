import * as React from 'react';

import { Button } from './Button';
import { Socket } from './Socket';
import Linkify from 'react-linkify';
import isImageUrl from 'is-image-url';

export function Content() {
    const [user_count, setCount] = React.useState('')
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
            Socket.on('users received', updateUsers);
            return () => {
                Socket.off('users received', updateUsers);
            }
        });
    }
    
    function getNewCount() {
        React.useEffect(() => {
            Socket.on('count received', updateCount);
            return () => {
                Socket.off('count received', updateCount);
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
        console.log('Received new user: ' + data['all_users']);
        setUsers(data['all_users']);
    }
    
    function updateCount(data) {
        console.log('Received new user: ' + data['user_count']);
        setCount(data['user_count']);
    }
    
    getNewuser();
    getNewCount();
    getNewMessage();


    
    return (
        <Linkify>
            <div className="chatbox">
                <h1>Messages!</h1>
                    <ul id="box">
                        {
                            messages.map((message, index) => {
                                isImageUrl(message) ?
                                    <li key={index}>--<img src={message}/></li>
                                    :
                                    <li id="mess" key={index}>__{message}</li>;
                            })
                        }
                    </ul>
                    <ul className="userList">
                        {
                            users.map((user, index) =>
                            <li key={index}>{user}</li>)
                        }
                    </ul>
            </div>
            <Button />
            <h2 className="users">Total users: {user_count}</h2>
        </Linkify>
    );
}