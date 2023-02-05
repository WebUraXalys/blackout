import React from 'react';
import {ButtonGroup, Typography} from "@mui/material";
import Button from "@mui/material/Button";

const FormCardConfirm = ({setFormIsSubmitted, sendData, handleClose}) => {


    const handleConfirm = (e) => {
        e.preventDefault()
        console.log(sendData)
        handleClose()
        setFormIsSubmitted(false)
    }

    return (
        <div>
            <form onSubmit={handleConfirm} style={{display: 'flex', flexDirection: 'column'}}>

                <Typography variant="h5" color="white" mb={1}>Your address is: </Typography>
                <Typography variant="h5" color="white" mb={2}>{sendData.city}, {sendData.street}, {sendData.number}</Typography>
                <Typography variant="h5" color="white" mb={2}>Group: G1</Typography>

                <ButtonGroup variant="outlined" fullWidth aria-label="outlined button group">
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
                    <Button disabled sx={{marginTop: 2, color: 'rgb(246,65,65)',
                        border: '1px solid rgba(246,65,65, .5)',
                        '&:hover': {
                            border: '1px solid rgb(246,65,65)'
                        }}}
                            size="large"
                            variant="outlined"
                            type="button"
                    >
                        Change
                    </Button>
                </ButtonGroup>
            </form>
        </div>
    );
};

export default FormCardConfirm;