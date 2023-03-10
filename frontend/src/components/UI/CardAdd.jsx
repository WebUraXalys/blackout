import React from 'react';
import {Card, CardActionArea, CardContent} from "@mui/material";
import Typography from "@mui/material/Typography";
import AddRoundedIcon from "@mui/icons-material/AddRounded.js";

const CardAdd = ({handleOpen}) => {

    return (
        <Card sx={{ height: 165, width: 180, background: '#48484a', margin: 0, border: '1px solid #ffd60a'}}>

            <CardActionArea sx={{textAlign: 'center', padding: '40px 30px'}} onClick={handleOpen}>

                <CardContent sx={{padding: 0}}>
                    <AddRoundedIcon sx={{fontSize: '50px', color: '#ffd60a'}}/>
                </CardContent>
                <CardContent sx={{padding: 0}}>
                    <Typography sx={{color: 'rgba(255,214,10,0.7)'}} variant="h5">
                        Add timer
                    </Typography>
                </CardContent>

            </CardActionArea>

        </Card>
    );
};

export default CardAdd;