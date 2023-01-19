import { Link } from 'react-router-dom';
import { useContext } from 'react';
import AuthContext from './context/AuthContext';


const Navbar = () => {
    const { user, logoutUser } = useContext(AuthContext);

    return ( 
        <nav className="navbar">
            <h1>Museum</h1>
            <div className="links">
                <Link to="/">Home</Link>
                {user && <button onClick={logoutUser}>Logout</button>}
                {!user && <Link to="/login">Login</Link>}
            </div>
        </nav>
     );
}
 
export default Navbar;
