import React from 'react';
import LocationForm from "../components/LocationForm.jsx";
import {Box} from "@mui/material";

const Home = () => {


    return (
        <>
            <Box sx={{zIndex: 100 ,color: 'black', width: '400px', margin: '0 auto', backgroundColor: '#fff', borderRadius: '10px'}}>
                <LocationForm/>
            </Box>
        </>
    );
};

export default Home;

