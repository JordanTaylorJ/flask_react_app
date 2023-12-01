
const Menu = () => {
    return(
        <div className=' p-4 text-lg container fixed z-40'>
            <button className='block hover:text-blue-200'>Profile</button>
            <button className='block hover:text-blue-200'>Logs</button>
            <button className='block hover:text-blue-200'>Aircraft</button>
            <button className='block hover:text-blue-200'>Logout</button>
        </div>
    )
}

export default Menu;