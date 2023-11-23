'use client'
import React, {useState} from 'react';

const Login = () => {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    return(
        <form className=''>
            <label> Username:
                <input className='border-0'/>
            </label>
            <label> Password:
                <input/>
            </label>
        </form>
    )
}

export default Login;