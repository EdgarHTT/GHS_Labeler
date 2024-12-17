import React from "react"

function DisplayBar({ content }) {
    return (
        <div> { content ? ( <div dangerouslySetInnerHTML={{ __html: content}} />
        ) : (
            <p>No content</p>
        )}
        </div>
    );
}

export default DisplayBar