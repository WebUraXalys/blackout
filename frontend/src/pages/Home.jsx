import React from 'react';
import useModalCard from "../components/ModalCard.jsx";
import LocationForm from "../components/LocationForm.jsx";
import {Grid} from "@mui/material";

const Home = () => {

    const {render} = useModalCard()
    // const [electricity, setElectricity] = useState(true)

    return (
        <div>
            {render}

            <Grid sx={{ flexGrow: 1 , flexWrap: 'wrap'}} container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
                <Grid item>
                    <LocationForm />
                </Grid>
            </Grid>

        </div>
    );
};

export default Home;

