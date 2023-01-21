import { useState, useEffect, useRef } from 'react'
import React from 'react'
import { useParams, useNavigate } from 'react-router-dom';
import axiosInstance from '../../services/axios';
import { Badge, Button, Center, Container, Spinner, Text, useColorModeValue, useToast } from '@chakra-ui/react';
import { AddUpdateTodoModal } from './AddUpdateTodoModal';

export const TodoDetail = () => {
    const [todo, setTodo] = useState({});
    const [loading, setLoading] = useState(true);
    const isMounted = useRef(false);
    const { todoId } = useParams()
    const navigate = useNavigate()
    const background = useColorModeValue("gray.300", "gray.600")
    const toast = useToast()

    const fetchTodo = () => {
        setLoading(true)
        axiosInstance.get(`/todo/${todoId}`)
            .then((res) => {
                setTodo(res.data)
            })
            .catch((error) => console.error(error))
            .finally(() => {
                setLoading(false);
            })
    }

    useEffect(() => {
        if (isMounted.current) return;
        fetchTodo();
        isMounted.current = true
    }, [todoId])

    const deleteTodo = () => {
        setLoading(true);
        axiosInstance.delete(`/todo/${todoId}`)
            .then(() => {
                toast({
                    title: "Todo deleted successfully",
                    status: "success",
                    isClosable: true,
                    duration: 5000,

                });
                navigate('/');
            }).catch((err) => {
                toast({
                    title: "Could not delete Todo",
                    status: "error",
                    isClosable: true,
                    duration: 5000,

                });
            })
            .finally(() => setLoading(false))
    }


    if (loading) {
        return (
            <Container mt={6}>
                <Center mt={6}>
                    <Spinner
                        thickness="4px"
                        speed="0.65s"
                        emptyColor="green.200"
                        color="green.500"
                        size="xl"
                    />
                </Center>
            </Container>
        )
    }

    return (
        <>
            <Container mt={6}>
                <Button colorScheme="gray" onClick={() => navigate('/', { replace: true })}>
                    Back
                </Button>
            </Container>
            <Container
                bg={background}
                minHeight="7rem"
                my={3}
                p={3}
                rounded="lg"
                alignItems="center"
                justifyContent="space-between">
                <Badge colorScheme={todo.status ? "green" : "purple"} align="right">{todo.status ? "Completed" : "Pending"}
                </Badge>
                <Text fontSize={22} align="center">{todo.title}</Text>


                <Text bg="gray.400" mt={2} p={2} rounded="lg">
                    {todo.description}
                </Text>
                <AddUpdateTodoModal
                    my={3}
                    editable={true}
                    defaultValues={{
                        title: todo.title,
                        description: todo.description,
                        status: todo.status
                    }}
                    onSuccess={fetchTodo} />
                <Button isLoading={loading} colorScheme="red" width="100%" onClick={deleteTodo}>
                    Delete
                </Button>

            </Container>
        </>
    )
}
