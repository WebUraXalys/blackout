import React from 'react';
import {Route, Routes} from "react-router-dom";
import Home from "../pages/Home.jsx";
import Timer from "../pages/Timer.jsx";
import Map from "../pages/Map.jsx";
import Meet from "../pages/Meet.jsx";
import Settings from "../pages/Settings.jsx";

const AppRouter = () => {
    return (
        <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/timer" element={<Timer/>}/>
            <Route path="/map" element={<Map/>}/>
            <Route path="/meet" element={<Meet/>}/>
            <Route path="/settings" element={<Settings/>}/>
        </Routes>
    );
};

export default AppRouter;