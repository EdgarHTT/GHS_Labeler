import React, { useState, useEffect } from 'react'
import axios, { formToJSON } from "axios"
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Accordion from 'react-bootstrap/Accordion'

function CommandBar() {
    const [query, setQuery] = useState("") // Compound search box
    const [response, setReponse] = useState(null) // To store fetched data
    const [error, setError] = useState(null) // handle errors

    // Handle input changes
    const handleChange = (e) => {
        const value = e.target.value // Gets value from input element
        setQuery(value) // Sets query with input value
        console.log(value) // Logs current value
    }

    // Handle submit
    const handleSubmit = (e) => {
        e.preventDefault() // Prevent page reload
        console.log("Submitted query:", query)
        axios.post("http://localhost:3000/fetchCompound", query, {
            headers: { 'Content-Type': 'application/json'}
        })
        .then((response) => {
            console.log('Response:', response.data)
        })
        .catch((error) => {
            console.error('Error submitting data:', error)
        })

    }

    return (
        <div>
            <Form onSubmit={handleSubmit}>
               <Form.Group className="mb-3" 
               controlId="formCompoundName">
                <Form.Control 
                    type="string" 
                    placeholder='Enter compound name'
                    value={query}
                    onChange={handleChange}
                />
                <Form.Text>
                    Fetch compound safety data.
                </Form.Text>
               </Form.Group>
               <Button variant="primary" type="submit" onClick={handleSubmit}>
                Fetch
               </Button>
            </Form>
            
            <Accordion defaultActiveKey="1">
                <Form>
                    <Accordion.Item eventKey="0">
                        <Accordion.Header>Label content</Accordion.Header>
                            <Accordion.Body>
                            <Form.Group className="mb-3" controlId="formProductId">
                                <Form.Label>Product Identifier</Form.Label>
                                <Form.Control type="id"/>
                            </Form.Group>

                            <Form.Group className="mb-3" controlId="formSignal">
                                <Form.Label>Signal Word</Form.Label>
                                <Form.Control type="signal"/>
                            </Form.Group>

                            <Form.Group className="mb-3" controlId="formHazards">
                                <Form.Label>Hazard Statements</Form.Label>
                                <Form.Control type="hazards"/>
                            </Form.Group>

                            <Form.Group className="mb-3" controlId="formPreStatements">
                                <Form.Label>Precautionary Statements</Form.Label>
                                <Form.Control type="precautionary"/>
                            </Form.Group>

                            <Form.Group className="mb-3" controlId="formSuppInfo">
                                <Form.Label>Supplier Information</Form.Label>
                                <Form.Control type="supp_info"/>
                            </Form.Group>

                            <Form.Group className="mb-3" controlId="formPictograms">
                                <Form.Label>Pictograms</Form.Label>
                                <Form.Control type="pictograms"/>
                            </Form.Group>
                            <Button variant="primary" type="submit">
                                Generate Label
                            </Button>
                            </Accordion.Body>
                    </Accordion.Item>
                </Form>
            </Accordion>


        </div>
    );
}

export default CommandBar