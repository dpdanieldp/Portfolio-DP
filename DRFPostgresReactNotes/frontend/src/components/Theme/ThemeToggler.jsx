import React from 'react'
import { Switch, useColorMode, FormLabel } from '@chakra-ui/react'

export const ThemeToggler = ({ showLabel = false, ...rest }) => {
    const { colorMode, toggleColorMode } = useColorMode();
    return (
        <>
            {showLabel && (
                <FormLabel htmlFor='theme-toggler' mb={0}>
                    Enable Dark Theme
                </FormLabel>
            )}
            <Switch
                id="theme-toggler"
                size="sm"
                isChecked={colorMode === "dark"}
                isDisabled={false}
                value={colorMode}
                colorScheme="blue"
                mr={2}
                onChange={toggleColorMode}
            // {...rest}
            />
        </>
    )
}
