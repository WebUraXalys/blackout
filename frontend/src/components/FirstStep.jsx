import React, { useCallback, useContext } from "react";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { AppContext } from "../Context";


export default function FirstStep() {

	const { formValues, handleChange, handleNext, variant, size } = useContext(AppContext);
	const { firstName, lastName, email, gender } = formValues;

	const isError = useCallback(() =>
		Object.keys({ firstName, lastName, email, gender }).some(
			(name) =>
				(formValues[name].required && !formValues[name].value) ||
				formValues[name].error
		),
		[formValues, firstName, lastName, email, gender])

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
						label="First Name"
						name="firstName"
						placeholder="Your first name"
						value={firstName.value}
						onChange={handleChange}
						error={!!firstName.error}
						helperText={firstName.error || " "}
						required={firstName.required}
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
						label="Last Name"
						name="lastName"
						placeholder="Your last name"
						value={lastName.value}
						onChange={handleChange}
						error={!!lastName.error}
						helperText={lastName.error || " "}
						required={lastName.required}
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
						label="Email"
						name="email"
						placeholder="Your email address"
						type="email"
						value={email.value}
						onChange={handleChange}
						error={!!email.error}
						helperText={email.error || " "}
						required={email.required}

					/>
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