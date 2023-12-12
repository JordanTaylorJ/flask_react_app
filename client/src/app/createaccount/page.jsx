'use client'
import React, {useState, useContext} from 'react';
import Link from "next/link"
import { UserContext } from '../context/user';

const CreateAccount = () => {

    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errors, setErrors] = useState('');
    const {setUser} = useContext(UserContext);

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch('/api/signup', {
            method: 'POST',
            headers: {
                'Content-Type':'application/json'
            },
            body: JSON.stringify({firstName, lastName, email, password})
        })
        .then(r => {
            if (r.ok) {
                r.json().then(r => setUser(r))
                setErrors('')
            }
            else {
                r.json().then(r => setErrors(r))
            }
        })
    }

    return(
        <main>
        <form 
            className='flex flex-wrap justify-center p-24'
            onSubmit={(e) => handleSubmit(e)}
        >
            <label> First Name:
                <input 
                    className='border-2 border-black'
                    onChange={(e) => setFirstName(e.target.value)}
                />
            </label>
            <label> Last Name:
                <input 
                    className='border-2 border-black'
                    onChange={(e) => setLastName(e.target.value)}
                />
            </label>
            <br/>
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
                Sign Up
            </button>
        </form>
        {errors ? 
            <h1>{errors}</h1>
            : 
            <></>
        }
        <Link className='text-sm' href='/login'>Login</Link>
        </main>
    )
}

export default CreateAccount;