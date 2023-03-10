import React, { useState } from "react";
import Box from "@mui/material/Box";
import Button from '@mui/material/Button';
import CancelIcon from '@mui/icons-material/Cancel';

export default function Success() {

	const [open, setOpen] = useState(true);

	const handleClose = () => setOpen(false);

	return (
		<>
			<Box>
				<Button onClick={handleClose}>
					<CancelIcon />
				</Button>
				Location created!
			</Box>
		</>
	);
}
