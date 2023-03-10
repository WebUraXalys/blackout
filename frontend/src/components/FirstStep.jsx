import React, { useCallback, useContext } from "react";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { AppContext } from "../Context";
import {Checkbox, FormControlLabel, FormHelperText} from "@mui/material";


export default function FirstStep() {

	const { formValues, handleChange, handleNext, variant, size } = useContext(AppContext);
	const { city, street, number, agreement } = formValues;

	const isError = useCallback(() =>
		Object.keys({ city, street, number, agreement }).some(
			(name) =>
				(formValues[name].required && !formValues[name].value) ||
				formValues[name].error
		),
		[formValues, city, street, number, agreement])

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
						label="City"
						name="city"
						placeholder="Lviv"
						value={city.value}
						onChange={handleChange}
						error={!!city.error}
						helperText={city.error || " "}
						required={city.required}
					/>
				</Grid>
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
						label="Street"
						name="street"
						placeholder="Skisna"
						value={street.value}
						onChange={handleChange}
						error={!!street.error}
						helperText={street.error || " "}
						required={street.required}
					/>
				</Grid>
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
						label="House number"
						name="number"
						placeholder="21B"
						value={number.value}
						onChange={handleChange}
						error={!!number.error}
						helperText={number.error || " "}
						required={number.required}
					/>
				</Grid>
				<Grid item xs={10}>
					<FormControlLabel sx={{
						'& .MuiFormControlLabel-label': {
							fontFamily: 'Rubik, sans-serif',
							color: '#48484a'
						}
					}}
									  control={
										  <Checkbox
											  size="small"
											  checked={agreement.value}
											  onChange={handleChange}
											  name="agreement"
											  color="primary"
											  required={agreement.required}
										  />
									  }
									  label="Agree to terms and conditions"
					/>
					<FormHelperText error={!!agreement.error}>
						{agreement.error}
					</FormHelperText>
				</Grid>
			</Grid>

			<Box sx={{ display: "flex", justifyContent: "space-around", p: 2 }}>
				<Button
					variant="contained"
					sx={{ mt: 1, width: '200px'}}
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