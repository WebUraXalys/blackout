import React, {useState} from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Modal from '@mui/material/Modal';
import FormCard from "./FormCard.jsx";
import FormCardConfirm from "./FormCardConfirm.jsx";


const ModalCard = () => {

    const [open, setOpen] = useState(false);
    const [formIsSubmitted, setFormIsSubmitted] = useState(false)
    const [data, getData] = useState({
        city: '',
        street: '',
        number: '',
    })
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    const submitForm = () => {
        setFormIsSubmitted(true);
    }
    const setData = (data) => {
        getData({
            city: data.city,
            street: data.street,
            number: data.number,
        })
    }

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
                    width: '30%',
                    height: '45%',
                    backdropFilter: 'blur(16px) saturate(180%)',
                    webkitBackdropFilter: 'blur(16px) saturate(180%)',
                    backgroundColor: 'rgba(17, 25, 40, 0.82)',
                    borderRadius: '12px',
                    border: '1px solid rgba(255, 255, 255, 0.2)',
                    p: 4
                }}>
                    {!formIsSubmitted
                        ? <FormCard submitForm={submitForm} onSubmit={setData}/>
                        : <FormCardConfirm setFormIsSubmitted={setFormIsSubmitted} data={data} handleClose={handleClose}/>
                    }
                </Box>
            </Modal>
        </Box>
    );
};

export default ModalCard;