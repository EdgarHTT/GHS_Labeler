import React from 'react'
import Button from 'react-bootstrap/Button';

function GenerateButton({ onSubmit }) {
    return (
        <Button
            variant="primary"
            onClick={onSubmit}
        >
            {'Click to generate'}
        </Button>
    );
}

export default GenerateButton;