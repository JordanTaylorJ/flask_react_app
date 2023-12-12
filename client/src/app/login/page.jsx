'use client'
import React, {useState, useContext} from 'react';
import Link from "next/link"
import { UserContext } from '../context/user';

const Login = () => {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errors, setErrors] = useState('');
    const {user, setUser} = useContext(UserContext);

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify({email, password})
        })
        .then(r => {
            if (r.ok) {
                r.json().then(r => setUser(r))
                setErrors('')
            }
            else {
                console.log('not okay', r)
                r.json().then(r => setErrors(r))
            }
        })
    }   

    return(
        <main>
            { user ?
            <h1>{user.first_name}</h1>
            :
            <></>
            }
        <form 
            className='flex flex-wrap justify-center p-24'
            onSubmit={(e) => handleSubmit(e)}
        >
            <label> Email:
                <input 
                    className='border-2 border-black'
                    onChange={(e) => setEmail(e.target.value)}
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
        {errors ? 
            <h1>{errors}</h1>
            : 
            <></>
        }
        <Link className='text-sm' href='/createaccount'>Create Account</Link>
        </main>
    )
}

export default Login;