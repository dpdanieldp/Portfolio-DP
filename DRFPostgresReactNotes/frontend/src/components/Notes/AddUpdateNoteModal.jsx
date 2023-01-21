import {
    Box,
    Button,
    FormControl,
    FormErrorMessage,
    FormLabel,
    Input,
    Modal,
    ModalBody,
    ModalCloseButton,
    ModalContent,
    ModalFooter,
    ModalHeader,
    ModalOverlay,
    Stack,
    Switch,
    Textarea,
    useColorModeValue,
    useDisclosure,
    useToast,
} from "@chakra-ui/react";
import { Controller, useForm } from "react-hook-form";
import { useParams } from "react-router-dom";
import useAxios from "../../utils/useAxios";

export const AddUpdateNoteModal = ({
    editable = false,
    defaultValues = {},
    onSuccess = () => { },
    ...rest
}) => {
    const { isOpen, onOpen, onClose } = useDisclosure();
    const api = useAxios()
    const toast = useToast();
    const { noteId } = useParams();
    const {
        handleSubmit,
        register,
        control,
        formState: { errors, isSubmitting },
    } = useForm({
        defaultValues: { ...defaultValues },
    });

    const onSubmit = async (values) => {
        try {
            if (editable) {
                await api.put(`/notes/${noteId}/`, values);
            } else {
                await api.post(`/notes/`, values);
            }
            toast({
                title: editable ? "Note Updated" : "Note Added",
                status: "success",
                isClosable: true,
                diration: 1500,
            });
            onSuccess();
            onClose();
        } catch (err) {
            console.error(err);
            toast({
                title: "Something went wrong. Please try again.",
                status: "error",
                isClosable: true,
                diration: 5000,
            });
        }
    };

    return (
        <Box {...rest}>
            <Button w="100%" colorScheme="green" onClick={onOpen}>
                {editable ? "Update" : "ADD NOTE"}
            </Button>
            <Modal
                closeOnOverlayClick={false}
                size="xl"
                onClose={onClose}
                isOpen={isOpen}
                isCentered
            >
                <ModalOverlay />
                <form onSubmit={handleSubmit(onSubmit)}>
                    <ModalContent>
                        <ModalHeader>{editable ? "Update Note" : "Add Note"}</ModalHeader>
                        <ModalCloseButton />
                        <ModalBody>
                            <FormControl isInvalid={errors.title}>
                                <Input
                                    placeholder="Note Title...."
                                    background={useColorModeValue("gray.300", "gray.600")}
                                    type="text"
                                    variant="filled"
                                    size="lg"
                                    mt={6}
                                    {...register("title", {
                                        required: "This is required field",
                                        minLength: {
                                            value: 5,
                                            message: "Title must be at least 5 characters",
                                        },
                                        maxLength: {
                                            value: 55,
                                            message: "Title must be at most 55 characters",
                                        },
                                    })}
                                />
                                <FormErrorMessage>
                                    {errors.title && errors.title.message}
                                </FormErrorMessage>
                            </FormControl>
                            <FormControl isInvalid={errors.body}>
                                <Textarea
                                    rows={5}
                                    placeholder="Note body...."
                                    background={useColorModeValue("gray.300", "gray.600")}
                                    type="text"
                                    variant="filled"
                                    size="lg"
                                    mt={6}
                                    {...register("body", {
                                        required: "This is required field",
                                        minLength: {
                                            value: 5,
                                            message: "Description must be at least 5 characters",
                                        },
                                        maxLength: {
                                            value: 200,
                                            message: "Description must be at most 200 characters",
                                        },
                                    })}
                                />
                                <FormErrorMessage>
                                    {errors.body && errors.body.message}
                                </FormErrorMessage>
                            </FormControl>
                            {/* <Controller
                                control={control}
                                name="status"
                                render={({ field }) => (
                                    <FormControl mt={6} display="flex" alignItems="center">
                                        <FormLabel htmlFor="is-done">Status</FormLabel>
                                        <Switch
                                            onChange={(e) => field.onChange(e.target.checked)}
                                            isChecked={field.value}
                                            id="id-done"
                                            size="lg"
                                            name="status"
                                            isDisabled={false}
                                            isLoading={false}
                                            colorScheme="green"
                                            variant="ghost"
                                        />
                                    </FormControl>
                                )}
                            /> */}
                        </ModalBody>
                        <ModalFooter>
                            <Stack direction="row" spacing={4}>
                                <Button onClick={onClose} disabled={isSubmitting}>
                                    Close
                                </Button>
                                <Button
                                    colorScheme="green"
                                    type="submit"
                                    isLoading={isSubmitting}
                                    loadingText={editable ? "Updating" : "Creating"}
                                >
                                    {editable ? "Update" : "Create"}
                                </Button>
                            </Stack>
                        </ModalFooter>
                    </ModalContent>
                </form>
            </Modal>
        </Box>
    );
};
