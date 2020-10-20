import * as React from 'react';
import { Socket } from './Socket';

function handleSubmit(event) {
    let newMessage = document.getElementById("message_input");
    let reg = new RegExp('(https?:\/\/[^ ]*\.(?:gif|png|jpg|jpeg))');
    let st = newMessage.value;
    let ans = reg.test(st);
    console.log(ans);
    if (ans == true) {
        let img = document.createElement('img');
        img.src = st;
        //newMessage.value = "<img src='" + st + "' />";
        document.getElementById('box').appendChild(img);
        console.log("hi");
        event.preventDefault();
    }

    
    
    
    Socket.emit('new message input', {
        'message': newMessage.value
    })
    console.log('Sent the message ' + newMessage.value + ' to server!');
    newMessage.value = '';
    
    event.preventDefault();
}

export function Button() {
    return (
        <form onSubmit={handleSubmit} className="submitButton">
            <input id="message_input" placeholder="Enter a message" className="input" autoComplete="off"></input>
            <button className="addButton">Chat!</button>
        </form>
    );
}