import React from 'react'
import Form from 'react-bootstrap/Form'

function SearchBar({ query, onSearchChange }) {
    return (
    <>
        <Form.Label htmlFor="searchQuery">Search Compound</Form.Label>
        <Form.Control
            type="Query"
            id="searchQuery"
            aria-describedby="queryHelpBlock"
            value={query}
            onChange={onSearchChange}
        />
        <Form.Text id="queryHelpBlock" muted>
            Search for a compound to generate it's label. You can use it's
            common name.
        </Form.Text>
    </>
    );
}

/* 
TODO: I plan to add the Auto-Complete Search Service from PubChem
to give live suggestions as the user is typing the compound 
in the search bar
*/
export default SearchBar;