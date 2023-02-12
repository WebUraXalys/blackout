import React, { useContext } from "react";
import Box from "@mui/material/Box";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemText from "@mui/material/ListItemText";
import Divider from "@mui/material/Divider";
import Button from "@mui/material/Button";
import { AppContext } from "../Context";

export default function Confirm() {
    const { formValues, handleBack, handleNext, variant } = useContext(AppContext);
    const {firstName, lastName, email ,city, street, number} = formValues;

    const handleSubmit = () => {
        let form = {};
        Object.keys(formValues).map((name) => {
            form = {
                ...form,
                [name]: formValues[name].value
            };
            return form;
        });
        console.log(form);
        handleNext();
    };
    return (
        <>
            <List disablePadding>
                <ListItem sx={{padding: '0 15px'}}>
                    <ListItemText
                        sx={{
                            '& .MuiListItemText-primary, .MuiListItemText-secondary': {
                                fontFamily: 'Rubik, sans-serif'
                            }
                        }}
                        primary={`First Name`}
                        secondary={firstName.value || "Not Provided"}
                    />
                </ListItem>

                <Divider />

                <ListItem sx={{padding: '0 15px'}}>
                    <ListItemText
                        sx={{
                            '& .MuiListItemText-primary, .MuiListItemText-secondary': {
                                fontFamily: 'Rubik, sans-serif'
                            }
                        }}
                        primary="Last Name"
                        secondary={lastName.value || "Not Provided"}
                    />
                </ListItem>

                <Divider />

                <ListItem sx={{padding: '0 15px'}}>
                    <ListItemText
                        sx={{
                            '& .MuiListItemText-primary, .MuiListItemText-secondary': {
                                fontFamily: 'Rubik, sans-serif'
                            }
                        }}
                        primary="Email Address"
                        secondary={email.value || "Not Provided"}
                    />
                </ListItem>

                <Divider />

                <ListItem sx={{padding: '0 15px'}}>
                    <ListItemText
                        sx={{
                            '& .MuiListItemText-primary, .MuiListItemText-secondary': {
                                fontFamily: 'Rubik, sans-serif'
                            }
                        }}
                        primary="City"
                        secondary={city.value || "Not Provided"}
                    />
                </ListItem>

                <Divider />

                <ListItem sx={{padding: '0 15px'}}>
                    <ListItemText
                        sx={{
                            '& .MuiListItemText-primary, .MuiListItemText-secondary': {
                                fontFamily: 'Rubik, sans-serif'
                            }
                        }}
                        primary="Street"
                        secondary={street.value || "Not Provided"}
                    />
                </ListItem>

                <Divider />

                <ListItem sx={{padding: '0 15px'}}>
                    <ListItemText
                        sx={{
                            '& .MuiListItemText-primary, .MuiListItemText-secondary': {
                                fontFamily: 'Rubik, sans-serif'
                            }
                        }}
                        primary="Number"
                        secondary={number.value || "Not Provided"}
                    />
                </ListItem>
            </List>

            <Box sx={{ display: "flex", justifyContent: "space-around", mt: 1, p: 2 }}>
                <Button variant={variant} sx={{ mr: 1 }} onClick={handleBack}>
                    Back
                </Button>
                <Button variant="contained" color="success" onClick={handleSubmit}>
                    Confirm & Send
                </Button>
            </Box>
        </>
    )
}
