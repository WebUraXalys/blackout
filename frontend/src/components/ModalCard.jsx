import React, {useState} from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Modal from '@mui/material/Modal';
import SendIcon from '@mui/icons-material/Send';
import TextField from '@mui/material/TextField';


const ModalCard = () => {
    const [open, setOpen] = React.useState(false);
    const [myFocus, setMyFocus] = useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    const [values, setValues] = useState({
        city: "",
        street: "",
        number: "",
    });
    const inputs = [
        {
            id: 1,
            name: "city",
            margin: "dense",
            variant: "outlined",
            size: "small",
            label: "City",
            pattern: "^[A-Za-z0-9]{3,14$}",
            type: "text",
            required: true,
            error: myFocus === true,
            helperText: "Write correct city(ex: Lviv)"
        },
        {
            id: 2,
            name: "street",
            margin: "dense",
            variant: "outlined",
            size: "small",
            label: "Street",
            pattern: "^[A-Za-z0-9]{2,16}$",
            type: "text",
            required: true,
            error: myFocus === true,
            helperText: "Write correct street(ex: Skisna)"
        },
        {
            id: 3,
            name: "number",
            margin: "dense",
            variant: "outlined",
            size: "small",
            label: "Number",
            pattern: "^[A-Za-z0-9]{3,10}$",
            type: "text",
            required: true,
            error: myFocus === true,
            helperText: "Write correct number(ex: 126)"
        }
    ]

    const handleSubmit = (e) => {
        e.preventDefault();

    }
    const handleFocus = (e) => {
        setMyFocus(true)
        console.log(e.target)
    }

    const onChange = (e) => {
        setValues({
            ...values,
            [e.target.name]: e.target.value
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

    console.log(values)
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
                    <form onSubmit={handleSubmit} style={{display: 'flex', flexDirection: 'column'}}>
                        {inputs.map((input) => <TextField
                            sx={style}
                            helperText={input.helperText || " "}
                            error={input.error}
                            key={input.id}
                            name={input.name}
                            margin={input.margin}
                            variant={input.variant}
                            size={input.size}
                            type={input.type}
                            label={input.label}
                            pattern={input.pattern}
                            required={input.required}
                            value={values[input.name]}
                            onChange={onChange}
                            onBlur={handleFocus}
                        />)}
                        <Button type="submit" sx={{marginTop: 2}} size="small" variant="outlined" endIcon={<SendIcon />}>
                            Submit
                        </Button>
                    </form>

                </Box>
            </Modal>
        </Box>
    );
};

export default ModalCard;