// import React, {useState} from 'react';
// import LocationList from "../components/LocationList.jsx";
// import LocationForm from "../components/LocationForm.jsx";

// const Timer = () => {

//     const [open, setOpen] = useState(false);
//     const handleOpen = () => {
//         setOpen(true);
//     }

//     const [locations, setLocations] = useState([
//         {id: 1, icon: 'home', title: "Home", electricity: false},
//         {id: 2, icon: 'work', title: "Work", electricity: true},
//     ])

//     const createLocation = (newLocation) => {
//         setLocations([...locations, newLocation])
//     }



//     return (
//         <div>
//             {open && (
//                 <LocationForm setOpen={setOpen} create={createLocation} setLocations={setLocations}/>
//             )}

//             <LocationList locations={locations} handleOpen={handleOpen}/>
//         </div>
//     );
// };

// export default Timer;
import React, { useState } from 'react';
import LocationList from "../components/LocationList.jsx";
import LocationForm from "../components/LocationForm.jsx";

const Timer = () => {
  const [open, setOpen] = useState(false);
  const handleOpen = () => {
    setOpen(true);
  }

  const [locations, setLocations] = useState([
    { id: 1, icon: 'home', title: "Home", electricity: false },
    { id: 2, icon: 'work', title: "Work", electricity: true },
  ])

  return (
    <div>
      {open && (
        <LocationForm setOpen={setOpen} setLocations={setLocations} />
      )}
      <LocationList locations={locations} handleOpen={handleOpen} />
    </div>
  );
};

export default Timer;
