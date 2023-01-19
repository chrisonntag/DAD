import { useParams, useNavigate } from 'react-router-dom';
import { useContext } from 'react';
import AuthContext from './context/AuthContext';
import React, { useState } from "react";
import useAPI from './useAPI';


const PostComment = () => {
    const { id } = useParams();
    const [commentTitle, setCommentTitle] = useState('');
    const [commentContent, setCommentContent] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const navigate = useNavigate();
    const { user } = useContext(AuthContext);


    const postComment = (e) => {
        const comment = { 'title': commentTitle, 'content': commentContent };

        setIsLoading(true);

        fetch('http://localhost:8000/api/items/' + id + '/comment/', {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(comment)
        }).then(() => {
            setIsLoading(false);
            navigate('/item/' + id);
        })
    }

    return (
        <>
            Logged in as {user.username}
            <form onSubmit={postComment}>
                <label htmlFor='title'>Title: </label>
                <input required name='title' type='text' value={commentTitle} onChange={(e) => setCommentTitle(e.target.value)} />
                <label htmlFor='content'>Content: </label>
                <textarea required value={commentContent} onChange={(e) => setCommentContent(e.target.value)}></textarea>
                {!isLoading && <input type='submit' value='Post Comment'/>}
                {isLoading && <input disabled type='submit' value='Post Comment'/>}
            </form>
        </>
    )
}

export default PostComment;
