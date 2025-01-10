import React, { useRef } from "react"

function DisplayBar({ content }) {
    
    const svgRef = useRef()
    
    const downloadSVG = () => {
        // SVG element to string
        const svgElement = svgRef.current
        const svgData = new XMLSerializer().serializeToString(svgElement)

        // Create a blob with the SVG data
        const blob = new Blob([svgData], { type: "image/svg+xml;charset=utf-8" })
        const url = URL.createObjectURL(blob)

        // Download link
        const link = document.createElement("a")
        link.href = url
        link.download = "GHS_Label.svg"
        document.body.appendChild(link)
        link.click()

        // Cleanup
        document.body.removeChild(link)
        URL.revokeObjectURL(url)
    }

    return (
        <div> { content ? (
        <div ref={svgRef} dangerouslySetInnerHTML={{ __html: content}}/>
        ) : (
            <p>No content</p>
        )}
        <br />
        <button onClick={downloadSVG}>Download Label</button>
        </div>
    );
}

export default DisplayBar