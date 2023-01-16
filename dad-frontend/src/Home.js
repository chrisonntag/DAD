import ItemsList from './ItemsList';
import useAPI from './useAPI.js';
import { useState } from 'react'


const Home = () => {
    const [isOnlyFavorites, setOnlyFavorites] = useState(false);
    const {data: items, isLoading, error} = useAPI(isOnlyFavorites ? 'http://localhost:8000/api/items/favorites/': 'http://localhost:8000/api/items/');

    const handleFavorites = () => {
        setOnlyFavorites(!isOnlyFavorites)
    }

    return ( 
        <div className="home">
            {error && <div>{error}</div>}
            {isLoading && <div>Loading...</div>}
            
            <button onClick={handleFavorites}>Show Favorites</button>
            <ItemsList items={items} />
        </div>
     );
}

export default Home;
