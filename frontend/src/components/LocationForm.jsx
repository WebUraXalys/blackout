import React from 'react';
import {Paper, Box} from "@mui/material";
import {Typography} from "@mui/material";
import HomeRoundedIcon from '@mui/icons-material/HomeRounded';
import FlashOffIcon from '@mui/icons-material/FlashOff';
import TimerOutlinedIcon from '@mui/icons-material/TimerOutlined';


const LocationForm = (props, {electricity}) => {


    return (

           electricity
               ? <Paper elevation={3} sx={{backgroundColor: '#20202194',margin: '5px auto',display: 'flex', justifyItems: 'center', alignItems: 'center', flexDirection: 'column', width: '200px', borderRadius: '15px'}}>
                <HomeRoundedIcon sx={{marginTop: '14px', backgroundColor: '#ffd60a', borderRadius: '5px', color: '#fff', fontSize: '60px', padding: '2px'}}/>
                <Typography variant="h5" sx={{color: '#ffd60a', margin: '12px 0'}}>Home</Typography>
                <Typography sx={{color: '#636366'}}>Time until blackout: </Typography>
                <Box sx={{display: 'flex', alignItems: 'center', margin: '6px 0 12px 0'}}>
                    <TimerOutlinedIcon sx={{color: '#ffd60a', marginRight: '5px'}}/>
                    <Typography sx={{color: '#ffd60a'}}>1h 28m</Typography>
                </Box>
              </Paper>

            : <Paper elevation={3} sx={{backgroundColor: '#20202194',margin: '5px auto',display: 'flex', justifyItems: 'center', alignItems: 'center', flexDirection: 'column', width: '200px', borderRadius: '15px'}}>
                <HomeRoundedIcon sx={{marginTop: '14px', backgroundColor: '#48484A', borderRadius: '5px', color: '#CCCABE', fontSize: '60px', padding: '2px'}}/>
                <Typography variant="h5" sx={{color: '#8E8E93', margin: '12px 0'}}>Home</Typography>
                <Typography sx={{color: '#636366'}}>Time before blackout: </Typography>
                <Box sx={{display: 'flex', alignItems: 'center', margin: '6px 0 12px 0'}}>
                    <FlashOffIcon sx={{color: '#FF453A'}}/>
                    <Typography sx={{color: '#8E8E93'}}>1h 28m</Typography>
                </Box>
            </Paper>
    );
};

export default LocationForm;