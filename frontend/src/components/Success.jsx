import React from "react";
import {Alert, Snackbar} from "@mui/material";

export default function Success() {

    const [open, setOpen] = React.useState(true);

    const handleClose = () => {
        setOpen(false);
    };

    return (
        <>
            <Snackbar open={open} autoHideDuration={5000} onClose={handleClose}>
                <Alert onClose={handleClose} variant="filled" elevation={6} severity="success" sx={{ width: '100%' }}>
                    This is a success message!
                    You will get an email with further instructions
                </Alert>
            </Snackbar>
        </>
    );
}
