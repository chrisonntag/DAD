import React, { Component } from 'react'
import { Link } from 'react-router-dom';


export default class ItemsList extends Component {
    constructor(props){
        super(props)
        this.state = {
            items: props.items
        }
    }

    renderItems(items) {
        if (items != null && items.length > 0) {
            return items.map((item, index) => (
                <>
                <div key={item.id}>
                    <Link to={`/item/${item.id}`}>
                        <h2>{item.name}</h2>
                        <img src={`https://picsum.photos/400?grayscale&random=${item.id}`} />
                    </Link>
                    <p>{item.description}</p>
                </div>
                </>
            ))
        } else {
            return []
        }
    };

    render() {
      const items = this.renderItems(this.props.items)
      return (
        <>
        <h1>Items</h1>
        <section>
            {items}
        </section>
        </>
      )
    }
}

