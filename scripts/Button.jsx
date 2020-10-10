import * as React from 'react';
import { Socket } from './Socket';

function handleSubmit(event) {
    let newMessage = document.getElementById("message_input");
    Socket.emit('new message input', {
        'message': newMessage.value
    })
    
    
    
    
    console.log('Sent the message ' + newMessage.value + ' to server!');
    newMessage.value = ''
    
    event.preventDefault();
}

export function Button() {
    return (
        <form onSubmit={handleSubmit} class="button">
            <input id="message_input" placeholder="Enter a message" class="input"></input>
            <button class="addButton">Add to DB!</button>
        </form>
    );
}
