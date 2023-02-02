import React from 'react';
import { MapContainer, TileLayer } from 'react-leaflet';
// import "../node_modules/leaflet/dist/leaflet.css";

const Map = () => {
    return (
        <MapContainer center={[49.288, 23.4162]} zoom={13} scrollWheelZoom={false}>
            <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
        </MapContainer>
    );
};

export default Map;