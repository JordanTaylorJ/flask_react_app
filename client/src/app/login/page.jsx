'use client'
import React, {useState, useContext} from 'react';
import Link from "next/link"
import { UserContext } from '../context/user';

const Login = () => {

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errors, setErrors] = useState('');
    const {setUser} = useContext(UserContext);

    console.log(username, password)
    return(
        <main>
        <form className='flex flex-wrap justify-center p-24'>
            <label> Username:
                <input 
                    className='border-2 border-black'
                    onChange={(e) => setUsername(e.target.value)}
                />
            </label>
            <label> Password:
                <input 
                className='border-2 border-black'
                onChange={(e) => setPassword(e.target.value)}
                />
            </label>
            <button>
                Sign In
            </button>
        </form>
        <h1></h1>
        <Link className='text-sm' href='/createaccount'>Create Account</Link>
        </main>
    )
}

export default Login;