import Link from 'next/link';


const Menu = () => {
    return(
        <div className=' p-4 text-lg container fixed z-40'>
            <Link className='block hover:text-blue-200'href='/'>Profile</Link>
            <Link className='block hover:text-blue-200' href='/logs'>Logs</Link>
            <Link className='block hover:text-blue-200' href='/'>Aircraft</Link>
            <button className='block hover:text-blue-200'>Logout</button>
        </div>
    )
}

export default Menu;