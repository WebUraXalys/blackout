import React, {useEffect, useState} from 'react';
import Button from "@mui/material/Button";
import {TextField} from "@mui/material";
import validation from "./Validation";

const FormCard = () => {

    const [values, setValues] = useState({
        city: "",
        street: "",
        number: "",
    })
    const [errors, setErrors] = useState({})

    const handleSubmit = (e) => {
        e.preventDefault();

        const errors = validation(values)

        if (errors) {
            setErrors(validation(values))
        }
    }
    useEffect(() => {
        if (errors.city === false && errors.street === false && errors.number === false){
            console.log(values)
        }
    }, [errors])

    const handleChange = (e) => {
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
        <form onSubmit={handleSubmit} style={{display: 'flex', flexDirection: 'column'}}>

            <TextField
                sx={style}
                error={Boolean(errors.city)}
                margin="dense"
                size="small"
                helperText={Boolean(errors.city) ? "Write your city(ex: Lviv)" : " "}
                label="City"
                name="city"
                value={values.city}
                onChange={handleChange}
            />
            <TextField
                sx={style}
                error={Boolean(errors.street)}
                margin="dense"
                size="small"
                helperText={Boolean(errors.street) ? "Write your street(ex: Skisna)" : " "}
                label="Street"
                name="street"
                value={values.street}
                onChange={handleChange}
            />
            <TextField
                sx={style}
                error={Boolean(errors.number)}
                margin="dense"
                size="small"
                helperText={Boolean(errors.number) ? "Write your number(ex: 21B)" : " "}
                label="Number"
                name="number"
                value={values.number}
                onChange={handleChange}
            />
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