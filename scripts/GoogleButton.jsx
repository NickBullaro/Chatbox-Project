import React from 'react';
import * as ReactDOM from 'react-dom';

import { Redirect } from 'react-router-dom';
import { Socket } from './Socket';
import { GoogleLogin } from 'react-google-login';
import { Content } from './Content';


const responseGoogle = (response) => {
  console.log(response);
}

function handleSubmit(response) {
    console.log(response.profileObj.name);
    console.log(response.profileObj.email);
    let name = response.profileObj.name;
    let email = response.profileObj.email;
    Socket.emit('new google user', {
        'name': name,
        'email': email
    });
    
    console.log('Sent the name ' + name + ' to server!');
    ReactDOM.render(<Content/>, document.getElementById('content'));
}




export function GoogleButton() {
    return (
                <GoogleLogin
                clientId="757847605849-7vlkasb74m9tjh95b3p6n1it3387u7th.apps.googleusercontent.com"
                buttonText="Login"
                onSuccess={handleSubmit}
                onFailure={responseGoogle}
                cookiePolicy={'single_host_origin'}/>
            );
}

 
