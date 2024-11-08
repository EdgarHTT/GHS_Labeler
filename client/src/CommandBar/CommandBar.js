import React, { useState } from 'react'
import SearchBar from './SearchBar/SearchBar'
import GenerateButton from './GenerateButton/GenerateButton'
import { fetchCompound } from './serverConnection/sendData.js'

function CommandBar() {
    // State to store the search query
    const [query, setQuery] = useState('');

    // Handle the change in the search input
    const handleSearchChange = (event) => {
        setQuery(event.target.value);
        // TODO: add the Auto-Complete API functionality
    };

    // Handle the submission of the form
    const handleSubmit = (e) => {
        e.preventDefault();
        fetchCompound(query);
        //TODO: I'll send the query to the backend perform the generation
    }
    return (
        <div>
            {/* Passing state and handler to Searchbar and GenerateButton */}
            <SearchBar query={query} onSearchChange={handleSearchChange} />
            <GenerateButton onSubmit={handleSubmit} />
        </div>
    );
}

export default CommandBar