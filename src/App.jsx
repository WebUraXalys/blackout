/* import { useState } from 'react' */
import './styles/App.css'
import MenuItem from "./components/MenuItem.jsx";
import home from "./assets/home-v.svg"
import meet from "./assets/meet-v.svg"
import map from "./assets/map-v.svg"
import settings from "./assets/settings-v.svg"
import timer from "./assets/timer.svg"
import logo from "./assets/logo_header.png"
// import LocationItem from "./components/LocationItem.jsx";

function App() {
  return (
    <div className="App">
      <div className="body">
          <header className="header">
            <div className="logo_d">
              <img src={logo} alt="Логотип Blackout" className="logo"/>
            </div>
            <hr className="header_line"/>
          </header>
          <section className="location-section">

          </section>
          <footer className="footer">
           <hr className="footer-line"/>
            <div className="menu">
              <MenuItem item={{title: "Дім", img: home}}/>
              <MenuItem item={{title: "Таймер", img: timer}}/>
              <MenuItem item={{title: "Мапа", img: map}}/>
              <MenuItem item={{title: "Зустріч", img: meet}}/>
              <MenuItem item={{title: "Налаштування", img: settings}}/>
            </div>
          </footer>
      </div>
    </div>
  )
}
export default App
