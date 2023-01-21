import { useEffect, useRef, useState } from 'react'
import { Box, Center, Container, Spinner } from '@chakra-ui/react'
import React from 'react'
import { NoteCard } from './NoteCard'
import { AddUpdateNoteModal } from './AddUpdateNoteModal'
import useAxios from '../../utils/useAxios'

export const NotesList = () => {
    const [notes, setNotes] = useState([])
    const [loading, setLoading] = useState(true)
    const isMounted = useRef(false)

    const api = useAxios()

    useEffect(() => {
        if (isMounted.current) return
        fetchNotes()

        isMounted.current = true
    }, [])

    const fetchNotes = () => {
        setLoading(true)
        api.get("/notes/")
            .then((res) => [
                setNotes(res.data)
            ]).catch((error) => {
                console.error(error)
            }).finally(() => {
                setLoading(false)
            })
    }

    return (
        <Container mt={9}>
            <AddUpdateNoteModal onSuccess={fetchNotes} />
            {loading ? (
                <Center mt={6}>
                    <Spinner
                        thickness="4px"
                        speed="0.65s"
                        emptyColor="green.200"
                        color="green.500"
                        size="xl"
                    />
                </Center>
            ) : (
                <Box mt={6}>
                    {notes.length > 0 ? (notes.map((note) => (
                        <NoteCard note={note} key={note.id} />
                    ))) : (<p align="center">You have no Notes yet</p>)}
                    {/* {notes?.map((note) => (
                        <NoteCard note={note} key={note.id} />
                    ))} */}
                </Box>
            )}

        </Container>
    )
}
