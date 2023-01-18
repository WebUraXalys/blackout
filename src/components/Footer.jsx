import React from 'react';
import MenuItem from "./MenuItem.jsx";
import home from "../assets/home-v.svg";
import timer from "../assets/timer.svg";
import map from "../assets/map-v.svg";
import meet from "../assets/meet-v.svg";
import settings from "../assets/settings-v.svg";

const Footer = () => {
    return (
        <footer className="footer">
            <hr className="footer-line"/>
            <nav className="menu">
                <MenuItem item={{title: "Дім", img: home}}/>
                <MenuItem item={{title: "Таймер", img: timer}}/>
                <MenuItem item={{title: "Мапа", img: map}}/>
                <MenuItem item={{title: "Зустріч", img: meet}}/>
                <MenuItem item={{title: "Налаштування", img: settings}}/>
            </nav>
        </footer>
    );
};

export default Footer;