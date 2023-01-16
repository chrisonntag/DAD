import ItemsList from './ItemsList';
import useAPI from './useAPI.js';

const Home = () => {
    const {data: items, isLoading, error} = useAPI('http://localhost:8000/api/items/?format=json');

    return ( 
        <div className="home">
            {error && <div>{error}</div>}
            {isLoading && <div>Loading...</div>}
            <ItemsList items={items} />
        </div>
     );
}

export default Home;
