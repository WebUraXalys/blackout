import React from 'react';
import {TextField} from "@mui/material";

const Meet = () => {

    let day, l, timing;
    const addEntries = (e) => {
        e.preventDefault()

        let weekDay = document.querySelector('#day').value
        let gr1 = "g" + document.getElementById('gr1').value;
        let gr2 = "g" + document.getElementById('gr2').value;

        l = {
            "entries": [{
                "day": ["mon", "thr", "sun"],
                "g1": [1, 0, 2, 1, 0, 2],
                "g2": [0, 2, 1, 0, 2, 1],
                "g3": [2, 1, 0, 2, 1, 0]
            },
                {
                    "day": ["tue", "fr"],
                    "g1": [0, 2, 1, 0, 2, 1],
                    "g2": [2, 1, 0, 2, 1, 0],
                    "g3": [1, 0, 2, 1, 0, 2]
                },
                {
                    "day": ["wed", "sat"],
                    "g1": [2, 1, 0, 2, 1, 0],
                    "g2": [1, 0, 2, 1, 0, 2],
                    "g3": [0, 2, 1, 0, 2, 1]
                },]
        }

        for (let i in l["entries"]) {
            if(l["entries"][i]["day"].includes(weekDay)){
                day = l["entries"][i]
                console.log(day[gr1]);
            }
        }

        timing = [
            "1:00-5:00",
            "5:00-9:00",
            "9:00-13:00",
            "13:00-17:00",
            "17:00-21:00",
            "21:00-1:00"
        ]

        for (let i = 0; i < 6; i++) {
            if (day[gr1][i] !== 1 && day[gr2][i] !== 1) {
                console.log(`Групи можуть зустрітись в ${timing[i]}`);

                if (day[gr1][i] === 2) {
                    console.log(`Зверніть увагу! У користувачів ${gr1} світла може не бути`);
                }

                if (day[gr2][i] === 2) {
                    console.log(`Зверніть увагу! У користувачів ${gr2} світла може не бути`);
                }
            }
        }

    }
    document.addEventListener("DOMContentLoaded", () => {
        document.getElementById('button').addEventListener("click", addEntries);
    });

    return (
        <>
            <TextField/>
        </>
    );
};

export default Meet;