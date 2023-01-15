import {useState, useEffect} from 'react';


const useAPI = (url) => {
    const [data, setData] = useState(null);
    const [isPending, setIsPending] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(url)
            .then(res => res.json())
            .then(data => setData(data.data));
    }, [url])

    return {data, isPending, error};
}

export default useAPI;
