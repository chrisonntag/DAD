import { Link } from 'react-router-dom';

const ItemsList = ({items}) => {
    
    return ( 
        <div className="items-list">
            <h2>Items</h2>
            {items}
        </div>
     );
}
 
export default ItemsList;
