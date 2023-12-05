import React, {useState, useEffect} from 'react';

const UserProvider = ({children}) => {
    const [user, setUser] = useState('');

    useEffect = (() => {
        fetch('/auth')
        .then(response => {
            if (response.ok) {
                response.json().then(currentUser => setUser(currentUser))
            }
        })
    }, []);

    return(
        <UserContext.Provider value={{user, setUser}}>
            {children}
        </UserContext.Provider>
    )
}

export {UserContext, UserProvider};
