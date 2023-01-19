import { useParams } from 'react-router-dom';
import { useContext } from 'react';
import useAPI from './useAPI';
import PostComment from './PostComment.js';
import AuthContext from './context/AuthContext';


const ItemDetail = () => {
    const { id } = useParams();
    const { data: item, isLoading, error } = useAPI('http://localhost:8000/api/items/' + id + '/');
    const { data: comments, commentsLoading, commentsError } = useAPI('http://localhost:8000/api/items/' + id + '/comment/');
    const { user } = useContext(AuthContext);


    return (
        <div className='item'>
            {isLoading && <div>Loading ...</div>}
            {error && <div>{error}</div>}
            {!isLoading &&
            <>
            <section className='item-detail'>
                <h1>{item.name}</h1>
                <img src={`https://picsum.photos/400?grayscale&random=${item.id}`} />
                <p>{item.description}</p>
            </section>

            {!commentsLoading &&
            <section className='item-comments'>
                <h2>Comments</h2>
                {user && <PostComment />}
                {comments != null && comments.length > 0 && comments.map((comment, index) => (
                    <div key={comment.id} className={`comment-${comment.id}`}>
                        <h3>{comment.title}</h3>
                        <h4>{comment.user.username} on {new Date(comment.date).toLocaleDateString("en-US")}</h4>
                        <p>{comment.content}</p>
                    </div>
                ))}
            </section>
            }

            </>
            }
        </div>
    )
}

export default ItemDetail;
