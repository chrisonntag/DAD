import { useParams, useNavigate } from 'react-router-dom';
import useAPI from './useAPI';
import PostComment from './PostComment.js';


const ItemDetail = () => {
    const { id } = useParams();
    const { data: item, isLoading, error } = useAPI('http://localhost:8000/api/items/' + id + '?format=json');
    const { data: comments, commentsLoading, commentsError } = useAPI('http://localhost:8000/api/items/' + id + '/comment?format=json');
    const navigate = useNavigate();


    function renderComments(comments) {
        if (comments != null && comments.length > 0) {
            comments.map((comment, index) => (
                <>
                <div className={`comment-${comment.id}`}>
                    <h3>{comment.title}</h3>
                    <h4>by {comment.user} on {comment.date}</h4>
                    <p>{comment.content}</p>
                </div>
                </>
            ))
        }
    }

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
                <PostComment />
                {comments != null && comments.length > 0 && comments.map((comment, index) => (
                    <>
                    <div className={`comment-${comment.id}`}>
                        <h3>{comment.title}</h3>
                        <h4>by {comment.user} on {comment.date}</h4>
                        <p>{comment.content}</p>
                    </div>
                    </>
                ))}
            </section>
            }

            </>
            }
        </div>
    )
}

export default ItemDetail;
