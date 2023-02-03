import './styles/App.css'
import Footer from "./components/Footer.jsx";
import Header from "./components/Header.jsx";
import {BrowserRouter as Router} from "react-router-dom"
import AppRouter from "./components/AppRouter";

function App() {
  return (
    <div className="App">
        <Router>
            <Header/>
            <div className="contend">
              <AppRouter/>
            </div>
            <Footer/>
        </Router>
    </div>
  )
}
export default App;
