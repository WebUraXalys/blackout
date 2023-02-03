import React from 'react';
import Button from "@mui/material/Button";


const FormCard = () => {

    // const style = {
    //     input: { color: 'white'},
    //     '& label': {color: '#48484A'},
    //     '.MuiFormHelperText-root': {color: '#48484A'},
    //     '& label.Mui-focused': {
    //         color: '#fff',
    //     },
    //     '& .MuiOutlinedInput-root': {
    //         '& fieldset': {
    //             borderColor: '#48484A',
    //         },
    //         '&:hover fieldset': {
    //             transition: '.4s ease-in-out',
    //             borderColor: 'white',
    //         },
    //         '&.Mui-focused fieldset': {
    //             borderColor: 'white',
    //         },
    //     },
    // }

    return (
        <form style={{display: 'flex', flexDirection: 'column'}}>


            <Button sx={{marginTop: 2, color: '#ffd60a',
                border: '1px solid rgba(255,214,10,0.55)',
                '&:hover': {
                    border: '1px solid #ffd60a'
                }}}
                    size="large"
                    variant="outlined"
                    type="submit"
            >
                Submit
            </Button>
        </form>
    );
};

export default FormCard;