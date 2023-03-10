import React, {useState} from 'react';
import {Card, CardActionArea, CardContent} from "@mui/material";
import Typography from "@mui/material/Typography";
import HomeOutlinedIcon from "@mui/icons-material/HomeOutlined.js";
import ElectricBoltOutlinedIcon from "@mui/icons-material/ElectricBoltOutlined.js";

const CardTemplate = ({name}) => {

    const [open, setOpen] = useState(false);
    const handleOpen = () => setOpen(true);

    return (
        <Card sx={{ height: 165, width: 180, background: '#48484a', margin: 0}}>

            <CardActionArea sx={{textAlign: 'center', padding: '5px'}} onClick={handleOpen}>

                <CardContent sx={{display: 'flex',alignItems: 'center', flexDirection: 'column', padding: 0}}>
                    <HomeOutlinedIcon sx={{fontSize: '50px', color: '#8e8e91', padding: '0'}}/>
                    <Typography sx={{color: '#8e8e91'}} variant="h7">
                        {name}
                    </Typography>
                </CardContent>
                <CardContent sx={{display: 'flex',alignItems: 'center', justifyContent: 'center', padding: '10px 0 5px 0'}}>
                    <ElectricBoltOutlinedIcon sx={{fontSize: '25px', color: '#0a8f37'}}/>
                    <Typography sx={{color: '#8e8e91'}} variant="h7">
                        13:00-17:00
                    </Typography>
                </CardContent>
                <CardContent sx={{padding: 0}}>
                    <Typography sx={{color: '#2a2a2f'}} variant="h7">
                        Until blackout
                    </Typography>
                    <Typography sx={{color: 'rgba(255,214,10,0.7)'}} variant="h6">
                        3 hours
                    </Typography>
                </CardContent>

            </CardActionArea>
        </Card>
    );
};

export default CardTemplate;