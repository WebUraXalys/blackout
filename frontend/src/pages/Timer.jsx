import React, {useState} from 'react';
import Modal from "@mui/material/Modal";
import {Box} from "@mui/material";
import LocationForm from "../components/LocationForm.jsx";
import CardAdd from "../components/UI/CardAdd.jsx";

const Timer = () => {

    const [open, setOpen] = useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    const style = {
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 400,
        bgcolor: 'background.paper',
        border: '2px solid #000',
        boxShadow: 24,
        p: 4,
    };

    return (
        <div className="grid-container">
            <CardAdd handleOpen={handleOpen}/>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={style}>
                    <LocationForm/>
                </Box>
            </Modal>
        </div>
    );
};

export default Timer;