import { Badge, Flex, Text, useColorModeValue } from '@chakra-ui/react'
import React from 'react'
import { useNavigate } from 'react-router-dom'

export const NoteCard = ({ note }) => {
    const navigate = useNavigate()
    return (
        <Flex bg={useColorModeValue("gray.300", "gray.600")}
            minHeight="3rem"
            my={3}
            p={3}
            rounded="lg"
            alignItems={"center"}
            justifyContent="space-between"
            _hover={{
                opacity: 0.9,
                cursor: "pinter",
                transform: "translateY(-3px)"
            }}
            onClick={() => navigate(`/${note.id}`, { replace: true })}
        >
            <Text>{note.title}</Text>
            {/* <Badge colorScheme={todo.status ? "green" : "purple"}>{todo.status ? "Completed" : "Pending"}
            </Badge> */}

        </Flex>
    )
}