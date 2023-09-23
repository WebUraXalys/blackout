import React, {useState} from 'react';
import {Card, CardActionArea, CardContent, CardMedia} from "@mui/material";
import Typography from "@mui/material/Typography";
import ElectricBoltOutlinedIcon from "@mui/icons-material/ElectricBoltOutlined.js";
import HomeRoundedIcon from "@mui/icons-material/HomeRounded.js";
import WorkRoundedIcon from "@mui/icons-material/WorkRounded.js";
import SchoolIcon from '@mui/icons-material/School';
import LocalGroceryStoreIcon from '@mui/icons-material/LocalGroceryStore';
import FitnessCenterRoundedIcon from '@mui/icons-material/FitnessCenterRounded';
import LocalHotelRoundedIcon from '@mui/icons-material/LocalHotelRounded';
import BlockIcon from "@mui/icons-material/Block.js";

const CardTemplate = ({location}) => {

    const [open, setOpen] = useState(false);
    const handleOpen = () => setOpen(true);

    const style = {
        fontSize: '50px',
        color: '#8e8e91',
        padding: '0',
    };

    const statusIcon = (status) => {
        switch (status) {
            case "home":
                return <HomeRoundedIcon sx={style}/>;
            case "work":
                return <WorkRoundedIcon sx={style}/>;
            case "gym":
                return <FitnessCenterRoundedIcon sx={style}/>;
            case "market":
                return <LocalGroceryStoreIcon sx={style}/>;
            case "hotel":
                return <LocalHotelRoundedIcon sx={style}/>;
            case "school":
                return <SchoolIcon sx={style}/>;
            default:
                return <BlockIcon sx={{fontSize: '50px', color: '#de0047', padding: '0'}}/>;
        }
    };

    return (
        <Card sx={{ height: 165, width: 180, background: '#48484a', margin: 0, border: '1px solid #ffd60a'}}>

            <CardActionArea sx={{textAlign: 'center', padding: '5px'}} onClick={handleOpen}>

                <CardContent sx={{display: 'flex',alignItems: 'center', flexDirection: 'column', padding: 0}}>
                    <CardMedia>
                        {statusIcon(location.icon)}
                    </CardMedia>
                    <Typography sx={{color: '#8e8e91'}} variant="h7">
                        {location.title}
                    </Typography>
                </CardContent>
                <CardContent sx={{display: 'flex',alignItems: 'center', justifyContent: 'center', padding: '10px 0 5px 0'}}>
                    <ElectricBoltOutlinedIcon sx={{fontSize: '25px', color: '#0a8f37'}}/>
                    <Typography sx={{color: '#8e8e91'}} variant="h7">
                        {/*{location.electricity}*/}
                        false
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