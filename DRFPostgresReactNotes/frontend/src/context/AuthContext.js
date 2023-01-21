import jwt_decode from "jwt-decode";
import { createContext, useState, useEffect } from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import { Flex, Spinner } from '@chakra-ui/react';



const AuthContext = createContext()

export default AuthContext;


export const AuthProvider = ({ children }) => {

    let [authTokens, setAuthTokens] = useState(() => localStorage.getItem('authTokens') ? JSON.parse(localStorage.getItem('authTokens')) : null)
    let [user, setUser] = useState(() => localStorage.getItem('authTokens') ? jwt_decode(localStorage.getItem('authTokens')) : null)
    let [loading, setLoading] = useState(true)

    const navigate = useNavigate()
    const location = useLocation()

    let loginUser = async (username, password) => {
        // e.preventDefault()
        let response = await fetch('http://127.0.0.1:8000/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'username': username, 'password': password })
        })
        let data = await response.json()

        if (response.status === 200) {
            setAuthTokens(data)
            setUser(jwt_decode(data.access))
            localStorage.setItem('authTokens', JSON.stringify(data))
            navigate('/', { replace: true, state: { from: location } })
        } else {
            alert('Something went wrong!')
        }
    }

    const logoutUser = () => {
        setAuthTokens(null)
        setUser(null)
        localStorage.removeItem('authTokens')
        navigate('/login', { replace: true, state: { from: location } })

    }


    const contextData = {
        user: user,
        authTokens: authTokens,
        setAuthTokens: setAuthTokens,
        setUser, setUser,
        loginUser: loginUser,
        logoutUser: logoutUser,
    }

    useEffect(() => {
        if (authTokens) {
            setUser(jwt_decode(authTokens.access))
        }
        setLoading(false)



    }, [authTokens, loading])

    return (
        <AuthContext.Provider value={contextData}>
            {loading ? (
                <Flex
                    height="100vh"
                    alignItems="center"
                    justifyContent="center">
                    <Spinner
                        thickness="4px"
                        speed="0.65s"
                        emptyColor="blue.200"
                        color="blue.500"
                        size="xl"
                    />
                </Flex>
            ) : children}
        </AuthContext.Provider>
    )
}
