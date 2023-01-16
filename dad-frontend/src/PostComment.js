import { useParams, useNavigate } from 'react-router-dom';
import React, { useState } from "react";
import useAPI from './useAPI';


const PostComment = () => {
    const { id } = useParams();
    const [commentTitle, setCommentTitle] = useState('');
    const [commentContent, setCommentContent] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const navigate = useNavigate();

    const postComment = (e) => {
        e.preventDefault();
        const comment = { commentTitle, commentContent };

        setIsLoading(true);

        fetch('http://localhost:8000/api/items/' + id + '/comment', {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(comment)
        }).then(() => {
            setIsLoading(false);
            navigate.push('/item/' + id);
        })
    }

    return (
        <>
            <form onSubmit={postComment}>
                <label for='title'>Title: </label>
                <input required name='title' type='text' value={commentTitle} onChange={(e) => setCommentTitle(e.target.value)} />
                <label for='content'>Content: </label>
                <textarea required value={commentContent} onChange={(e) => setCommentContent(e.target.value)}></textarea>
                {!isLoading && <input type='submit' value='Post Comment'/>}
                {isLoading && <input disabled type='submit' value='Post Comment'/>}
            </form>
        </>
    )
}

export default PostComment;
