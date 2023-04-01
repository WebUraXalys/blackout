import React, {useCallback, useContext, useState} from 'react';
import {Button, TextField, ToggleButton, ToggleButtonGroup} from "@mui/material";
import HomeRoundedIcon from "@mui/icons-material/HomeRounded.js";
import WorkRoundedIcon from "@mui/icons-material/WorkRounded.js";
import FitnessCenterRoundedIcon from "@mui/icons-material/FitnessCenterRounded.js";
import SchoolIcon from "@mui/icons-material/School.js";
import LocalGroceryStoreIcon from "@mui/icons-material/LocalGroceryStore.js";
import LocalHotelRoundedIcon from "@mui/icons-material/LocalHotelRounded.js";
import {styled} from "@mui/material/styles";
import Grid from "@mui/material/Grid";
import CloseRoundedIcon from '@mui/icons-material/CloseRounded';
import {AppContext} from "../Context.jsx";

const LocationForm = ({setOpen, create}) => {
	const { formValues, handleChange, variant, size } = useContext(AppContext);
	const { city, street, number } = formValues;

	const isError = useCallback(() =>
			Object.keys({ city, street, number }).some(
				(name) =>
					(formValues[name].required && !formValues[name].value) ||
					formValues[name].error
			),
		[formValues, city, street, number])

	const addNewPost = (e) => {
		e.preventDefault()
		let form = {};

		const newLocation = {
			...locationForm, id: Date.now()
		}
		create(newLocation)
		setLocationForm({city: '',
			street: '',
			number: '',
			title: '',
			icon: null})
		Object.keys(formValues).map((name) => {
			form = {
				...form,
				[name]: formValues[name].value
			};
			return form;
		});
		city.value = ''
		street.value = ''
		number.value = ''
		console.log(form);
		setOpen(false)
	}

	const handleSwitch = (e, newAlignment) => {
		setAlignment(newAlignment)
		setLocationForm({...locationForm, icon: newAlignment})
	};

	const [alignment, setAlignment] = useState('');

	const [locationForm, setLocationForm] = useState({
		city: '',
		street: '',
		number: '',
		title: '',
		icon: null,
	});

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
	// background: 'white', padding: '20px'
    return (
		<form style={{
			position: 'absolute',
			borderRadius: '10px',
			top: '50%',
			left: '50%',
			transform: 'translate(-50%, -50%)',
			width: 400,
			backgroundColor: 'white',
			border: '1px solid #111',
			boxShadow: 24,
			p: 4,
			zIndex: 100
		}}>
			<CloseRoundedIcon sx={{cursor: 'pointer', position: 'absolute', top: '5px', right: '5px'}} onClick={() => setOpen(false)}/>
			<Grid sx={{p: 4}} justifyContent="center" container spacing={1}>
				<Grid item xs={6} sm={6}>
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
				<Grid item xs={6} sm={6}>
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
				<Grid item xs={6} sm={6}>
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
				<Grid item xs={6} sm={6}>
					<TextField
						sx={{
							'& .MuiInputLabel-root, .MuiInputBase-root': {
								fontFamily: 'Rubik, sans-serif'
							}
						}}
						variant={variant}
						size={size}
						fullWidth
						label="Title"
						name="title"
						placeholder="Home"
						value={locationForm.title}
						onChange={e => setLocationForm({...locationForm, title: e.target.value})}
						// error={!!title.error}
						// helperText={title.error || " "}
						// required={title.required}
					/>
				</Grid>
				<StyledToggleButtonGroup
				color="primary"
				value={alignment}
				exclusive
				onChange={handleSwitch}
				aria-label="Platform"
				>
					<ToggleButton value='home'><HomeRoundedIcon/></ToggleButton>
					<ToggleButton value='work'><WorkRoundedIcon/></ToggleButton>
					<ToggleButton value='gym'><FitnessCenterRoundedIcon/></ToggleButton>
					<ToggleButton value='school'><SchoolIcon/></ToggleButton>
					<ToggleButton value='market'><LocalGroceryStoreIcon/></ToggleButton>
					<ToggleButton value='hotel'><LocalHotelRoundedIcon/></ToggleButton>
			</StyledToggleButtonGroup>
				<Button disabled={isError()} onClick={!isError() ? addNewPost : () => null} variant={"contained"}>Submit</Button>
			</Grid>
		</form>

);
};

export default LocationForm;

// <form style={{background: 'white', padding: '20px'}}>
//
// 	<TextField value={locationForm.title} onChange={e => setLocationForm({...locationForm, title: e.target.value})} label="Title" variant="outlined" placeholder="Location name" size="medium"/>
//
// 	<StyledToggleButtonGroup
// 		color="primary"
// 		value={alignment}
// 		exclusive
// 		onChange={handleSwitch}
// 		aria-label="Platform"
// 	>
// 		<ToggleButton value='home'><HomeRoundedIcon/></ToggleButton>
// 		<ToggleButton value='work'><WorkRoundedIcon/></ToggleButton>
// 		<ToggleButton value='gym'><FitnessCenterRoundedIcon/></ToggleButton>
// 		<ToggleButton value='school'><SchoolIcon/></ToggleButton>
// 		<ToggleButton value='market'><LocalGroceryStoreIcon/></ToggleButton>
// 		<ToggleButton value='hotel'><LocalHotelRoundedIcon/></ToggleButton>
// 	</StyledToggleButtonGroup>
// 	<Button onClick={addNewPost} variant={"contained"}>Submit</Button>
// </form>