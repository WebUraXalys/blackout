import React from 'react';
import LocationForm from "../components/LocationForm.jsx";
import {Box} from "@mui/material";

const Home = () => {


    return (
        <>
            <Box sx={{color: 'white', width: '300px', margin: '0 auto', backgroundColor: 'gray'}}>
                <LocationForm/>

            </Box>
        </>
    );
};

export default Home;

