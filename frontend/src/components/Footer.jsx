import React from 'react';
import {NavLink} from 'react-router-dom';
import home from "../assets/home-v.svg";
import timer from "../assets/timer.svg";
import map from "../assets/map-v.svg";
import meet from "../assets/meet-v.svg";
import settings from "../assets/settings-v.svg";

const Footer = () => {

    const activeLink = "menu__link menu__link-active";
    const link = "menu__link";

    return (
        <footer className="footer">
            <hr className="footer-line"/>
            <ul className="menu">

                <li className="menu__el">
                    <NavLink className={({isActive}) => isActive ? activeLink : link} to="/">
                        <img className="svg_menu" src={home} alt="picture"/>
                        <p className="menu__text">Дім</p>
                    </NavLink>
                </li>

                <li className="menu__el">
                    <NavLink className={({isActive}) => isActive ? activeLink : link} to="/timer">
                        <img className="svg_menu" src={timer} alt="picture"/>
                        <p className="menu__text">Таймер</p>
                    </NavLink>
                </li>

                <li className="menu__el">
                    <NavLink className={({isActive}) => isActive ? activeLink : link} to="/map">
                        <img className="svg_menu" src={map} alt="picture"/>
                        <p className="menu__text">Мапа</p>
                    </NavLink>
                </li>

                <li className="menu__el">
                    <NavLink className={({isActive}) => isActive ? activeLink : link} to="/meet">
                        <img className="svg_menu" src={meet} alt="picture"/>
                        <p className="menu__text">Зустріч</p>
                    </NavLink>
                </li>

                <li className="menu__el">
                    <NavLink className={({isActive}) => isActive ? activeLink : link} to="/settings">
                        <img className="svg_menu" src={settings} alt="picture"/>
                        <p className="menu__text">Налаштування</p>
                    </NavLink>
                </li>

            </ul>
        </footer>
    );
};

export default Footer;