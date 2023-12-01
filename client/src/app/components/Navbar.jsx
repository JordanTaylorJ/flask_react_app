'use client'
import React, {useState} from 'react';
import Menu from './Menu';

const Navbar = () => {

    const [isOpen, setIsOpen] = useState(false);

    return(
        <nav className='flex flex-wrap p-4 text-lg container fixed'>
        <div className='block'>
        <button onClick={() => setIsOpen(!isOpen)} type="button" className="block justify-right p-2 w-10 h-10 hover:text-blue-200">
            <svg className="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
                <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M1 1h15M1 7h15M1 13h15"/>
            </svg>
        </button>
        {isOpen ? <Menu/> : <></> }
        </div>
        </nav>
    )
}
export default Navbar;



