import React, { useState } from 'react';
import LocationList from "../components/LocationList.jsx";
import LocationForm from "../components/LocationForm.jsx";
import CardTemplate from '../components/UI/CardTemplate.jsx';
import HomeRoundedIcon from "@mui/icons-material/HomeRounded.js";
import {Card, CardActionArea, CardContent, CardMedia} from "@mui/material";
import Typography from "@mui/material/Typography";
import ElectricBoltOutlinedIcon from "@mui/icons-material/ElectricBoltOutlined.js";

function Home() {

		const [open, setOpen] = useState(false);
    const handleOpen = () => {
        setOpen(true);
    }

	    const [locations, setLocations] = useState([
        {id: 1, icon: 'home', title: "Home", electricity: false}
    ])

	     return (
			<div className="div main_container_home">
			{/* // 	<div>
      //       <LocationList locations={locations}/>
      //  	 </div> */}
         <div className="container">
            <Card sx={{ height: 165, width: 180, display: 'flex', background: '#48484a', margin: '15px 23.5%', border: '1px solid #ffd60a'}}>

            <CardActionArea sx={{textAlign: 'center', padding: '5px'}} onClick={handleOpen}>

                <CardContent sx={{display: 'flex',alignItems: 'center', flexDirection: 'column', padding: 0}}>
                    <CardMedia>
                      <HomeRoundedIcon/>
                    </CardMedia>
                    <Typography sx={{color: '#8e8e91'}} variant="h7">
                      Home
                    </Typography>
                </CardContent> 
                <CardContent sx={{display: 'flex',alignItems: 'center', justifyContent: 'center', padding: '10px 0 5px 0'}}>
                    <ElectricBoltOutlinedIcon sx={{fontSize: '25px', color: '#0a8f37'}}/>
                    <Typography sx={{color: '#8e8e91'}} variant="h7">
                        {/*{location.electricity}*/}
                        false
                    </Typography>
                </CardContent>
                <CardContent sx={{padding: 0}}>
                    <Typography sx={{color: '#2a2a2f'}} variant="h7">
                        Until blackout
                    </Typography>
                    <Typography sx={{color: 'rgba(255,214,10,0.7)'}} variant="h6">
                        3 hours
                    </Typography>
                </CardContent>

            </CardActionArea>
        </Card>
            {/* <CardAdd handleOpen={handleOpen}/> */}
        </div>
		</div>
    );


// const [showModal, setShowModal] = useState(false);
// const [firstName, setFirstName] = useState('');
// const [lastName, setLastName] = useState('');
// const [email, setEmail] = useState('');

// const handleConfirm = () => {
// 	// create a new component with the input data
// 	const newComponent = <NewComponent firstName={firstName} lastName={lastName} email={email} />;
// 	// do something with the new component
// 	console.log(newComponent);
// 	// close the modal
// 	setShowModal(false);
// }

// return (
// 	<div>
// 		<button onClick={() => setShowModal(true)}>Open Modal</button>
// 		{showModal && (
// 			<div className="modal">
// 				<div className="modal-content">
// 					<h2>Enter your information</h2>
// 					<label htmlFor="first-name">First Name:</label>
// 					<input type="text" id="first-name" value={firstName} onChange={(e) => setFirstName(e.target.value)} />
// 					<label htmlFor="last-name">Last Name:</label>
// 					<input type="text" id="last-name" value={lastName} onChange={(e) => setLastName(e.target.value)} />
// 					<label htmlFor="email">Email:</label>
// 					<input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} />
// 					<div className="button-group">
// 						<button onClick={() => setShowModal(false)}>Cancel</button>
// 						<button onClick={handleConfirm}>Confirm</button>
// 					</div>
// 				</div>
// 			</div>
// 		)}
// 	</div>
// );
// }

// function NewComponent({ firstName, lastName, email }) {
// 	return (
// 		<div>
// 			<h2>New Component</h2>
// 			<p>First Name: {firstName}</p>
// 			<p>Last Name: {lastName}</p>
// 			<p>Email: {email}</p>
// 		</div>
// 	);
}

export default Home;