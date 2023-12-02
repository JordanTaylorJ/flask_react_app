import Link from 'next/link';


const Menu = (setIsOpen) => {
    return(
        <div className=' p-4 text-lg container fixed z-40'>
            <Link className='block hover:text-blue-200'href='/profile' onClick={(() => setIsOpen(false))}>Profile</Link>
            <Link className='block hover:text-blue-200' href='/logs' onClick={(() => setIsOpen(false))}>Logs</Link>
            <Link className='block hover:text-blue-200' href='/aircraft' onClick={(() => setIsOpen(false))}>Aircraft</Link>
            <button className='block hover:text-blue-200'>Logout</button>
        </div>
    )
}

export default Menu;