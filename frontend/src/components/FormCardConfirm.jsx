import React, {useState} from 'react';
import {Typography, TextField, Box, ToggleButtonGroup, ToggleButton as MuiToggleButton} from "@mui/material";
import Button from "@mui/material/Button";
import HomeRoundedIcon from '@mui/icons-material/HomeRounded';
import FitnessCenterRoundedIcon from '@mui/icons-material/FitnessCenterRounded';
import WorkRoundedIcon from '@mui/icons-material/WorkRounded';
import ShoppingCartRoundedIcon from '@mui/icons-material/ShoppingCartRounded';
import RoomIcon from '@mui/icons-material/Room';
import SchoolIcon from '@mui/icons-material/School';
import { styled } from '@mui/material/styles';

const FormCardConfirm = ({setFormIsSubmitted, data, handleClose, setLocationName, setIcon}) => {

    const [name, setName] = useState("")

    const handleName = (e) => {
        setName(e.target.value)
        console.log(name)
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        //console.log(name, data)
        setFormIsSubmitted(false)
        setLocationName(name)
        setIcon(alignment)
        handleClose()

    }
    const [alignment, setAlignment] = useState('');

    const handleAlignment = (event, newAlignment) => {
        setAlignment(newAlignment);
        console.log(typeof(alignment))
    };

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

    const StyledToggleButtonGroup = styled(ToggleButtonGroup)(({ theme }) => ({
        '& .MuiToggleButtonGroup-grouped': {
            margin: theme.spacing(1),
            color: '#48484A',

            '&:not(:first-of-type)': {
                // borderRadius: theme.shape.borderRadius,
                borderRadius: '50%',
            },
            '&:first-of-type': {
                borderRadius: '50%',
            },


        },
    }));

    const ToggleButton = styled(MuiToggleButton)({
        "&.Mui-selected": {
            color: "#ffd60a",
            backgroundColor: 'transparent'
        },
        "&:hover": {
            color: "#ffd60a",
            transition: '.2s ease-in-out',
        }
    });

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

                    <StyledToggleButtonGroup
                        size="small"
                        value={alignment}
                        exclusive
                        onChange={handleAlignment}
                        aria-label="text alignment"
                    >
                        <ToggleButton value="HomeRoundedIcon" aria-label="right aligned">
                            <HomeRoundedIcon />
                        </ToggleButton>
                        <ToggleButton value="WorkRoundedIcon" aria-label="right aligned">
                            <WorkRoundedIcon />
                        </ToggleButton>
                        <ToggleButton value="FitnessCenterRoundedIcon" aria-label="right aligned">
                            <FitnessCenterRoundedIcon />
                        </ToggleButton>
                        <ToggleButton value="RoomIcon" aria-label="right aligned">
                            <RoomIcon />
                        </ToggleButton>
                        <ToggleButton value="SchoolIcon" aria-label="right aligned">
                            <SchoolIcon />
                        </ToggleButton>
                        <ToggleButton value="ShoppingCartRoundedIcon" aria-label="right aligned">
                            <ShoppingCartRoundedIcon />
                        </ToggleButton>

                    </StyledToggleButtonGroup>
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