import { Box, Button, Flex, Stack, Text, useColorModeValue } from '@chakra-ui/react'
import React, { useContext } from 'react'
// import { useAuth } from '../../hooks/useAuth'
import { Outlet } from 'react-router-dom'
import { ThemeToggler } from '../Theme/ThemeToggler'
import AuthContext from '../../context/AuthContext';

export const NavBar = () => {
    // const { logout } = useAuth()
    let { user, logoutUser } = useContext(AuthContext)

    return (
        <Box minHeight="100vh">
            <Flex
                as="nav"
                alignItems="center"
                justifyContent="space-between"
                wrap="wrap"
                p={2}
                bg={useColorModeValue("blue.300", "blue.600")}
                color="white"
            >
                <Text as="h2" fontSize={24} fontWeight="bold">  NOTES </Text>
                <Stack direction="row" align="center" spacing={4}>
                    <ThemeToggler size="lg" align="right" />
                    {user && <Button onClick={logoutUser} colorScheme="blue">Logout</Button>}
                    {/* <Button onClick={logoutUser} colorScheme="green">Logout</Button> */}
                </Stack>
            </Flex>
            <Outlet />
        </Box>
    )
}
