import Link from "next/link"

export default function Home() {

  let user = false

  
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-12">
      {user
      ? 
        <h1>Welcome User</h1>
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
