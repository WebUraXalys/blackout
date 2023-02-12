import React, { useCallback, useContext } from "react";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { AppContext } from "../Context";

export default function SecondStep() {
    const {formValues, handleChange, handleBack, handleNext, variant, margin} = useContext(AppContext);
    const {city, street, phone, number} = formValues;

    const isError = useCallback(
        () =>
            Object.keys({city, street, phone, number}).some(
                (name) =>
                    (formValues[name].required && !formValues[name].value) ||
                    formValues[name].error
            ),
        [formValues, city, street, phone, number]
    );

    return (
        <>
            <Grid container spacing={2}>
                <Grid item xs={12}>
                    <TextField
                        variant={variant}
                        margin={margin}
                        fullWidth
                        label="City"
                        name="city"
                        placeholder="Lviv"
                        value={city.value}
                        onChange={handleChange}
                        error={!!city.error}
                        helperText={city.error}
                        required={city.required}
                    />
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        variant={variant}
                        margin={margin}
                        fullWidth
                        label="Street"
                        name="street"
                        placeholder="Skisna"
                        value={street.value}
                        onChange={handleChange}
                        error={!!street.error}
                        helperText={street.error}
                        required={street.required}
                    />
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        variant={variant}
                        margin={margin}
                        fullWidth
                        label="Number"
                        name="number"
                        placeholder="21B"
                        value={number.value}
                        onChange={handleChange}
                        error={!!number.error}
                        helperText={number.error}
                        required={number.required}
                    />
                </Grid>
                {/*<Grid item xs={12}>*/}
                {/*    <FormControlLabel*/}
                {/*        control={*/}
                {/*            <Checkbox*/}
                {/*                checked={agreenemt.value}*/}
                {/*                onChange={handleChange}*/}
                {/*                name="agreenemt"*/}
                {/*                color="primary"*/}
                {/*                required={agreenemt.required}*/}
                {/*            />*/}
                {/*        }*/}
                {/*        label="Agree to terms and conditions"*/}
                {/*    />*/}
                {/*    <FormHelperText error={!!agreenemt.error}>*/}
                {/*        {agreenemt.error}*/}
                {/*    </FormHelperText>*/}
                {/*</Grid>*/}
            </Grid>

            <Box sx={{ display: "flex", justifyContent: "flex-end", mt: 3 }}>
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