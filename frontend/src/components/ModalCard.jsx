import React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Modal from '@mui/material/Modal';
import FormCard from "./FormCard.jsx";


const ModalCard = () => {

    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);





    return (
        <Box sx={{display: 'flex', justifyContent: 'center'}}>
            <Button sx={{margin: '10px 0', color: '#ffd60a',
                border: '1px solid rgba(255,214,10,0.55)',
                '&:hover': {
                border: '1px solid #ffd60a',
                },
            }} onClick={handleOpen}>Create location</Button>
            <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="modal-modal-title"
                aria-describedby="modal-modal-description"
            >
                <Box sx={{
                    position: 'absolute',
                    top: '50%',
                    left: '50%',
                    transform: 'translate(-50%, -50%)',
                    width: 400,
                    backdropFilter: 'blur(16px) saturate(180%)',
                    webkitBackdropFilter: 'blur(16px) saturate(180%)',
                    backgroundColor: 'rgba(17, 25, 40, 0.82)',
                    borderRadius: '12px',
                    border: '1px solid rgba(255, 255, 255, 0.125)',
                    p: 4
                }}>
                    <FormCard/>

                </Box>
            </Modal>
        </Box>
    );
};

export default ModalCard;