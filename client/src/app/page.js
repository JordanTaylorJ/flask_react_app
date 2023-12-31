'use client'
import Link from "next/link";
import React, {useContext} from 'react';

import { UserContext } from "./context/user";

export default function App() {

  const {user} = useContext(UserContext);
  console.log('user', user)
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-12">
      {user
      ? 
        <h1>Welcome {user.first_name}</h1>
      :
        <>
          <h1 className='text-3xl'>Digital Logbook</h1>
          <Link className='text-sm' href='/login'>Login</Link>
          <Link className='text-sm' href='/createaccount'>Create Account</Link>
        </>
      }
      
    </main>
  )
}
