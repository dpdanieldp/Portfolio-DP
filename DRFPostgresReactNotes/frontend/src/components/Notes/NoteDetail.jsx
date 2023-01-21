import { useState, useEffect, useRef } from 'react'
import React from 'react'
import { useParams, useNavigate } from 'react-router-dom';
import { Badge, Button, Box, Center, Container, Flex, Spinner, Spacer, Text, useColorModeValue, useToast } from '@chakra-ui/react';
import { AddUpdateNoteModal } from './AddUpdateNoteModal';
import useAxios from '../../utils/useAxios';

export const NoteDetail = () => {
    const [note, setNote] = useState({});
    const [loading, setLoading] = useState(true);
    const isMounted = useRef(false);
    const { noteId } = useParams()
    const navigate = useNavigate()
    const background = useColorModeValue("gray.300", "gray.600")
    const toast = useToast()

    const api = useAxios()

    const fetchNote = () => {
        setLoading(true)
        api.get(`/notes/${noteId}`)
            .then((res) => {
                setNote(res.data)
            })
            .catch((error) => console.error(error))
            .finally(() => {
                setLoading(false);
            })
    }

    useEffect(() => {
        if (isMounted.current) return;
        fetchNote();
        isMounted.current = true
    }, [noteId])

    const deleteNote = () => {
        setLoading(true);
        api.delete(`/notes/${noteId}`)
            .then(() => {
                toast({
                    title: "Note deleted successfully",
                    status: "success",
                    isClosable: true,
                    duration: 5000,

                });
                navigate('/');
            }).catch((err) => {
                toast({
                    title: "Could not delete Note",
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
                {/* <Badge colorScheme={todo.status ? "green" : "purple"} align="right">{todo.status ? "Completed" : "Pending"}
                </Badge> */}
                <Text fontSize={22} align="center">{note.title}</Text>


                <Text bg="gray.400" mt={2} p={2} rounded="lg">
                    {note.body}
                </Text>
                <Flex>
                    <Box p='4' >
                        <AddUpdateNoteModal
                            // my={3}
                            editable={true}
                            defaultValues={{
                                title: note.title,
                                body: note.body,
                                // status: todo.status
                            }}
                            onSuccess={fetchNote} />
                    </Box>
                    <Spacer />
                    <Box p='4' >
                        <Button isLoading={loading} colorScheme="red" width="100%" onClick={deleteNote}>
                            Delete
                        </Button>
                    </Box>
                </Flex>
                {/* <AddUpdateNoteModal
                    my={3}
                    editable={true}
                    defaultValues={{
                        title: note.title,
                        body: note.body,
                        // status: todo.status
                    }}
                    onSuccess={fetchNote} />
                <Button isLoading={loading} colorScheme="red" width="100%" onClick={deleteNote}>
                    Delete
                </Button> */}

            </Container>
        </>
    )
}
