import React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Modal from '@mui/material/Modal';
import {TextField} from "@mui/material";
import SendIcon from '@mui/icons-material/Send';

const ModalCard = () => {

    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);
    const [state, setState] = React.useState({
        city: "",
        street: "",
        number: ""
    })

    const handleChange = (e) => {
        const value = e.target.value;
        setState({
            ...state,
            [e.target.name]: value
        });
    }

    const sendData = () => {
        setState({
            city: "",
            street: "",
            number: ''
        })
    }

    const style = {
        input: { color: 'white'},
        '& label': {color: '#48484A'},
        '.MuiFormHelperText-root': {color: '#48484A'},
        '& label.Mui-focused': {
            color: '#48484A',
        },
        '& .MuiOutlinedInput-root': {
            '& fieldset': {
                borderColor: '#48484A',
            },
            '&:hover fieldset': {
                transition: '.4s ease-in-out',
                borderColor: 'white',
            },
            '&.Mui-focused fieldset': {
                borderColor: 'white',
            },
        },
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
                <form>
                    <Box
                        sx={{
                            position: 'absolute',
                            display: 'flex', justifyContent: 'center', flexDirection: 'column',
                            top: '50%',
                            left: '50%',
                            transform: 'translate(-50%, -50%)',
                            width: 300,
                            borderRadius: '10px',
                            p: 2,
                            backdropFilter: 'blur(16px) saturate(181%)',
                            "::webkitBackdropFilter": 'blur(16px) saturate(181%)',
                            backgroundColor: 'rgba(17, 25, 40, 0.96)',
                            border: '1px solid rgba(255, 255, 255, 0.125)',
                        }}
                    >
                        <TextField sx={style}
                            id="City"
                            label="City"
                            name="city"
                            helperText=" "
                            variant="outlined"
                            size="small"
                            type="text"
                            margin="dense"
                            onChange={handleChange}
                            value={state.city}
                        />
                        <TextField sx={style}
                            id="Street"
                            label="Street"
                            name="street"
                            helperText=" "
                            variant="outlined"
                            size="small"
                            type="text"
                            margin="dense"
                            onChange={handleChange}
                            value={state.street}

                        />
                        <TextField sx={style}
                            id="House number"
                            label="Number"
                            name="number"
                            helperText=" "
                            variant="outlined"
                            size="small"
                            type="text"
                            margin="dense"
                            onChange={handleChange}
                            value={state.number}

                        />
                        <Button
                            type="submit"
                            sx={{margin: '20px 0 10px'}}
                            variant="outlined"
                            endIcon={<SendIcon />}
                            onClick={sendData}
                        >
                            Send
                        </Button>
                    </Box>

                </form>
            </Modal>
        </Box>
    );
};

export default ModalCard;