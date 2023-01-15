import ItemsList from './ItemsList';
import useAPI from './useAPI.js';

const Home = () => {
    const {data: items, isPending, error} = useAPI('http://localhost:8000/test');

    return ( 
        <div className="home">
            {error && <div>{error}</div>}
            {isPending && <div>Loading...</div>}
            <ItemsList items={items} />
        </div>
     );
}

export default Home;
