import React from 'react';
import useModalCard from "../components/ModalCard.jsx";
import {Box} from "@mui/material";


const Home = () => {

    const {render, locationName, data, icon} = useModalCard()

    return (
        <div>
            {render}
            <Box sx={{color: 'red'}}>
                {locationName}
                {data.number}{data.city}{data.street}
                {icon}
            </Box>
        </div>
    );
};

export default Home;