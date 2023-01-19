import React from 'react';
import logo from "../assets/logo_header.png";

const Header = () => {
    return (
        <header className="header">
            <div className="logo_d">
                <img src={logo} alt="Логотип Blackout" className="logo"/>
            </div>
            <hr className="header_line"/>
        </header>
    );
};

export default Header;