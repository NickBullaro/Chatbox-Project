import * as React from 'react';
import * as Link from 'react-router-dom';

import { GoogleButton } from './GoogleButton';
import { Socket } from './Socket';



export function Login() {
    
    
    
    return (
    <div class="joinOuterContainer">
        <div class="joinInnerContainer">
        <h3 class="heading">Sign in with Google to continue!</h3>
            <GoogleButton/>
        </div>
    </div>
    );
}