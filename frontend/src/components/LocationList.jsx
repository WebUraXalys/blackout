import React from 'react';
import CardTemplate from "./UI/CardTemplate.jsx";
import CardAdd from "./UI/CardAdd.jsx";

const LocationList = ({locations, handleOpen}) => {
    return (
        <div className="grid-container">
            {locations.map((location) => <CardTemplate location={location} key={location.id}/>)}
            <CardAdd handleOpen={handleOpen}/>
        </div>
    );
};

export default LocationList;