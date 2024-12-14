import React, { useEffect, useState } from "react"

function DisplayBar() {
    const [content, setContent] = useState("")

    useEffect(() => {
        fetch('http://localhost:5000/generate')
            .then(response => response.text()) // Fetch the data as raw text to render raw HTML
            .then(html => setContent(html))
    }, [])

    return (
        <div dangerouslySetInnerHTML={{ __html: content}}></div>
    );
}

export default DisplayBar