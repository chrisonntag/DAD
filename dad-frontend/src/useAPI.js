import {useState, useEffect} from 'react';


const useAPI = (url) => {
    const [data, setData] = useState(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(url, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': 'Bearer ' + JSON.parse(localStorage.getItem('authTokens'))['access']
            }
        })
            .then(res => res.json())
            .then((data) => {
                setError(data.error)
                setData(data)
                setIsLoading(false)
            })
    }, [url])

    return {data, isLoading, error};
}

export default useAPI;
