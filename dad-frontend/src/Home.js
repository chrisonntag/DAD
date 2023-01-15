import ItemsList from './ItemsList';
import fetchAPI from './fetchAPI.js';

const Home = () => {
    const {data: items, isPending, error} = fetchAPI('http://localhost:8000/test');

    return ( 
        <div className="home">
            {error && <div>{error}</div>}
            {isPending && <div>Loading...</div>}
            <ItemsList items={items} />
        </div>
     );
}

export default Home;
