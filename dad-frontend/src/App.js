import Home from './Home';
import ItemDetail from './ItemDetail.js';
import Navbar from './Navbar.js';
import Login from './Login.js';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import './App.css';


function App() {
    return (
        <Router>
        <AuthProvider>
            <div className="App">
            <Navbar />
            <section className="content">
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/item/:id" element={<ItemDetail />} />
                </Routes>
            </section>
            </div>
        </AuthProvider>
      </Router>
    );
}

export default App;

