import React, {useState} from 'react';
import {Link} from 'react-router-dom'
import HomeOutlinedIcon from '@mui/icons-material/HomeOutlined';
import TimerOutlinedIcon from '@mui/icons-material/TimerOutlined';
import MapOutlinedIcon from '@mui/icons-material/MapOutlined';
import GroupsOutlinedIcon from '@mui/icons-material/GroupsOutlined';
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import {Box} from "@mui/material";
import '../styles/App.css'

const Footer = () => {

    const [selectedCategory, setSelectedCategory] = useState(0)

    return (
        <footer className="footer">
            <hr className="footer-line"/>
            <Box sx={{ width: '100%', background: 'none', display: 'flex', justifyContent: 'center'}}>
                <BottomNavigation
                    sx={{background: 'none', color: 'red'}}
                    showLabels
                    value={selectedCategory}
                    onChange={(event, newValue) => {
                        setSelectedCategory(newValue);
                    }}
                >
                    <BottomNavigationAction
                        component={Link}
                        to="/"
                        className="NavItem"
                        label="Home"
                        icon={<HomeOutlinedIcon />} />
                    <BottomNavigationAction
                        component={Link}
                        to="/timer"
                        className="NavItem"
                        label="Timer"
                        icon={<TimerOutlinedIcon />} />
                    <BottomNavigationAction
                        component={Link}
                        to="/map"
                        className="NavItem"
                        label="Map"
                        icon={<MapOutlinedIcon />} />
                    <BottomNavigationAction
                        component={Link}
                        to="/meet"
                        className="NavItem"
                        label="Meet"
                        icon={<GroupsOutlinedIcon />} />
                    <BottomNavigationAction
                        component={Link}
                        to="/settings"
                        className="NavItem"
                        label="Settings"
                        icon={<SettingsOutlinedIcon />} />
                </BottomNavigation>
            </Box>
        </footer>
    );
};

export default Footer;