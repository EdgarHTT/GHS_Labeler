import React, { useEffect, useState } from 'react'

function DisplayBar() {
    const [data, setdata] = useState(null);

    useEffect (() => {
        fetch('http://127.0.0.1:5000/compoundName')
            .then(response => response.json())
            .then(data => setdata(data.message))
            .catch(error => console.error("Error fetching data:", error))
    }, []);

    return (
        <div className="DisplayBar">
            <h1>{data? data : "Loading..."}</h1>
        </div>
    );
}

export default DisplayBar