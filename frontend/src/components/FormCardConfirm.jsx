import React, {useState} from 'react';
import {Typography, TextField, Box} from "@mui/material";
import Button from "@mui/material/Button";


const FormCardConfirm = ({setFormIsSubmitted, data, handleClose}) => {

    const [name, setName] = useState("")

    const handleName = (e) => {
        setName(e.target.value)
        console.log(name)
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        console.log(data, name)
        handleClose()
        setFormIsSubmitted(false)
    }

    const style = {
        input: { color: 'white'},
        '& label': {color: '#48484A'},
        '.MuiFormHelperText-root': {color: '#48484A'},
        '& label.Mui-focused': {
            color: '#fff',
        },
        '& .MuiOutlinedInput-root': {
            '& fieldset': {
                borderColor: '#48484A',
            },
            '& invalid': {
                borderColor: 'red'
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
        <div>
            <form onSubmit={handleSubmit} style={{display: 'flex', flexDirection: 'column'}}>

                <Box
                    color="#48484A"
                    mb={2}
                    width="85px"
                    sx={{
                        "& .my-address": {
                         display: "none"
                     },
                        "&:hover .my-address": {
                            display: "block"
                    },
                    '&:hover': {
                            color: '#ffd60a'
                    },
                    cursor: 'default'}}
                >
                    My address
                    <Typography
                        className="my-address"
                        variant="h6"
                        color="white"
                        mb={1}
                        sx={{borderRadius: '10px', padding: '0 5px', fontSize: '15px', display: 'none', position: 'absolute'}}
                    >
                        {data.city}, {data.street}, {data.number}
                    </Typography>
                </Box>


                <TextField
                    sx={style}
                    margin="dense"
                    size="small"
                    //helperText={Boolean(errors.name) ? "Name your location(ex: Home)" : " "}
                    label="Location name"
                    name="name"
                    value={name}
                    onChange={handleName}/>

                    <Button sx={{marginTop: 2, color: 'rgb(27,176,30)',
                        border: '1px solid rgba(27,176,30, 0.5)',
                        '&:hover': {
                            border: '1px solid rgb(27,176,30)'
                        }}}
                            size="large"
                            variant="outlined"
                            type="submit"
                    >
                        Confirm
                    </Button>
            </form>
        </div>
    );
};

export default FormCardConfirm;


// <Button disabled sx={{marginTop: 2, color: 'rgb(246,65,65)',
//     border: '1px solid rgba(246,65,65, .5)',
//     '&:hover': {
//         border: '1px solid rgb(246,65,65)'
//     }}}
//         size="large"
//         variant="outlined"
//         type="button"
// >
//     Change
// </Button>