import React from 'react'
import Form from 'react-bootstrap/Form'

function SearchBar() {
    return (
    <>
        <Form.Label htmlFor="searchQuery">Select Compound</Form.Label>
        <Form.Control
            type="Query"
            id="searchQuery"
            aria-describedby="queryHelpBlock"
        />
        <Form.Text id="queryHelpBlock" muted>
            Search for a compound to generate it's label. You can use their
            common name...
        </Form.Text>
    </>
    );
}

export default SearchBar;