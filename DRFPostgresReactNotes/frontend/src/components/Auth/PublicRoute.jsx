import React, { useEffect, useState, useContext } from 'react'
import { useLocation, useNavigate } from 'react-router-dom';
import AuthContext from '../../context/AuthContext';
// import { useAuth } from '../../hooks/useAuth'

export const PublicRoute = (props) => {
    const { children } = props;
    const { user } = useContext(AuthContext)
    // const auth = useAuth()
    const navigate = useNavigate()
    const location = useLocation()
    const [isVerified, setIsVerified] = useState(false)

    useEffect(() => {
        if (user) {
            navigate('/', { replace: true, state: { from: location } })

        } else {
            setIsVerified(true)
        }
    }, [user, location, navigate])

    if (!isVerified) {
        return null
    }
    return (
        <>{children}</>
    )
}
