import React, {useCallback, useContext, useState} from "react";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { AppContext } from "../Context";
import { styled } from '@mui/material/styles';
import {ToggleButton, ToggleButtonGroup} from "@mui/material";
import HomeRoundedIcon from '@mui/icons-material/HomeRounded';
import WorkRoundedIcon from '@mui/icons-material/WorkRounded';
import FitnessCenterRoundedIcon from '@mui/icons-material/FitnessCenterRounded';
import ShoppingCartRoundedIcon from '@mui/icons-material/ShoppingCartRounded';
import SchoolRoundedIcon from '@mui/icons-material/SchoolRounded';
import LocalHotelRoundedIcon from '@mui/icons-material/LocalHotelRounded';
import RestaurantMenuRoundedIcon from '@mui/icons-material/RestaurantMenuRounded';
import LocalGasStationRoundedIcon from '@mui/icons-material/LocalGasStationRounded';
import LocalCarWashRoundedIcon from '@mui/icons-material/LocalCarWashRounded';

export default function SecondStep() {
    const {formValues, handleChange, handleBack, handleNext, variant, size} = useContext(AppContext);
    const { location, icon } = formValues;

    const isError = useCallback(
        () =>
            Object.keys({location, icon}).some(
                (name) =>
                    (formValues[name].required && !formValues[name].value) ||
                    formValues[name].error
            ),
        [formValues, location, icon]
    );

    const [alignment, setAlignment] = useState('home');

    const handleSwitch = (e, newAlignment) => {
        setAlignment(newAlignment)
    };


    const StyledToggleButtonGroup = styled(ToggleButtonGroup)(({ theme }) => ({
        '& .MuiToggleButtonGroup-grouped': {
            margin: theme.spacing(0.5),
            border: 0,
            '&.Mui-disabled': {
                border: 0,
            },
            '&:not(:first-of-type)': {
                borderRadius: theme.shape.borderRadius,
            },
            '&:first-of-type': {
                borderRadius: theme.shape.borderRadius,
            },
        },
    }));

    return (
        <>
            <Grid justifyContent="center" container spacing={1}>
                <Grid item xs={12} sm={10}>
                    <TextField
                        sx={{
                            '& .MuiInputLabel-root, .MuiInputBase-root': {
                                fontFamily: 'Rubik, sans-serif'
                            }
                        }}
                        variant={variant}
                        size={size}
                        fullWidth
                        label="Location name"
                        name="location"
                        placeholder="Home"
                        value={location.value}
                        onChange={handleChange}
                        error={!!location.error}
                        helperText={location.error || " "}
                        required={location.required}
                    />
                </Grid>
            </Grid>
            <StyledToggleButtonGroup
                sx={{
                    display: "flex",
                    flexWrap: 'wrap',
                    justifyContent: "center",
                }}
                color="primary"

                value={alignment}
                exclusive
                onChange={handleSwitch}
                aria-label="Platform"
            >
                <ToggleButton value="home"><HomeRoundedIcon/></ToggleButton>
                <ToggleButton value="work"><WorkRoundedIcon/></ToggleButton>
                <ToggleButton value="gym"><FitnessCenterRoundedIcon/></ToggleButton>
                <ToggleButton value="restaurant"><RestaurantMenuRoundedIcon/></ToggleButton>
                <ToggleButton value="sleepover"><LocalHotelRoundedIcon/></ToggleButton>
                <ToggleButton value="gas"><LocalGasStationRoundedIcon/></ToggleButton>
                <ToggleButton value="market"><ShoppingCartRoundedIcon/></ToggleButton>
                <ToggleButton value="wash"><LocalCarWashRoundedIcon/></ToggleButton>
                <ToggleButton value="school"><SchoolRoundedIcon/></ToggleButton>
            </StyledToggleButtonGroup>

            <Box sx={{ display: "flex", justifyContent: "space-around", mt: 1, p: 2 }}>
                <Button onClick={handleBack} sx={{ mr: 1 }}>
                    Back
                </Button>
                <Button
                    variant="contained"
                    disabled={isError()}
                    color="primary"
                    onClick={!isError() ? handleNext : () => null}
                >
                    Next
                </Button>
            </Box>
        </>
    )
}