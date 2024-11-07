import React from 'react'
import { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';

function GenerateButton() {
    const [isGenerating, setGenerating] = useState(false);

    useEffect(() => {
        function simulateNetworkRequest() {
            return new Promise((resolve) => setTimeout(resolve, 2000));
        }

        if (isGenerating) {
            simulateNetworkRequest().then(() => {
                setGenerating(false);
            });
        }
    }, [isGenerating])

    const handleClick = () => setGenerating(true);

    return (
        <Button
            variant="primary"
            disabled={isGenerating}
            onClick={!isGenerating ? handleClick : null}
        >
            {isGenerating ? 'Generating...' : 'Click to generate'}
        </Button>
    );
}

export default GenerateButton;