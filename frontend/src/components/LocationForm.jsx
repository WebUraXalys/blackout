import React, { useContext } from "react";
import Box from "@mui/material/Box";
import Stepper from "@mui/material/Stepper";
import Step from "@mui/material/Step";
import StepLabel from "@mui/material/StepLabel";
import Typography from "@mui/material/Typography";
import FirstStep from "./FirstStep";
import SecondStep from "./SecondStep";
import Confirm from "./Confirm";
import Success from "./Success";
import { AppContext } from "../Context";

const labels = ["First Step", "Second Step", "Confirmation"];

const handleSteps = (step) => {
    switch (step) {
        case 0:
            return <FirstStep/>
        case 1:
            return <SecondStep/>
        case 2:
            return <Confirm/>
        default:
            throw new Error("Unknown step");
    }
};
export default function StepForm() {
    const { activeStep } = useContext(AppContext);

    return (
        activeStep === labels.length
            ? (<Success />)
            : (<div style={{ borderRadius: '7px'}}>
                <Box>
                    <Typography variant="h4" align="center" sx={{fontFamily: 'Rubik, sans-serif', padding: '10px 0'}}>
                        Registration
                    </Typography>
                </Box>
                <Stepper activeStep={activeStep} sx={{ py: 2 }} alternativeLabel>
                    {labels.map((label) => (
                        <Step sx={{
                            '& 	.MuiStepLabel-label': {
                                fontFamily: 'Rubik, sans-serif'
                            }
                        }} key={label}>
                            <StepLabel>{label}</StepLabel>
                        </Step>
                    ))}
                </Stepper>

                {handleSteps(activeStep)}
            </div>)
)
}