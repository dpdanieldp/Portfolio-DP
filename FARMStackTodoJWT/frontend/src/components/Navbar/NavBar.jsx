import { Box, Button, Flex, Stack, Text, useColorModeValue } from '@chakra-ui/react'
import React from 'react'
import { useAuth } from '../../hooks/useAuth'
import { Outlet } from 'react-router-dom'
import { ThemeToggler } from '../Theme/ThemeToggler'

export const NavBar = () => {
    const { logout } = useAuth()
    return (
        <Box minHeight="100vh">
            <Flex
                as="nav"
                alignItems="center"
                justifyContent="space-between"
                wrap="wrap"
                p={2}
                bg={useColorModeValue("green.300", "green.600")}
                color="white"
            >
                <Text as="h2" fontSize={24} fontWeight="bold"> TODO LIST </Text>
                <Stack direction="row" align="center" spacing={4}>
                    <ThemeToggler size="lg" align="right" />
                    <Button onClick={logout} colorScheme="green">Logout</Button>
                </Stack>
            </Flex>
            <Outlet />
        </Box>
    )
}
