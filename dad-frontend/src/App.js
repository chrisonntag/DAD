import Home from './Home';
import ItemDetail from './ItemDetail.js';
import Navbar from './Navbar.js';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import './App.css';

function App() {
    return (
        <Router>
            <div className="App">
            <Navbar />
            <section className="content">
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/item/:id" element={<ItemDetail />} />
                </Routes>
            </section>
            </div>
      </Router>
    );
}

export default App;

