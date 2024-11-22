import { useState, useEffect } from "react"

const useSendquery = ("http://127.0.0.1:5000".concat(endpoint), query) => {
    const [data, setData] = useState(null)

    useEffect(() => {
        fetch(endpoint), {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }, 
            body: JSON.stringify({query})
        }
        .then((res) => res.json())
        .then((data) => setData(data))
    }, [endpoint])

    return [data]
}

export default useSendquery