import React, { useState } from 'react'
import axios from "axios"
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Accordion from 'react-bootstrap/Accordion'

function CommandBar() {
    // Compound search box
    const [query, setQuery] = useState("")
    
    // To store form data
    const [content, setFormContent] = useState({
        id: " ",
        signal: " ",
        hazards: " ",
        precautionary: " ",
        supp_info: " ",
        pictograms: " ",
    })

    // handle errors
    const [error, setError] = useState(null)

    // Accordion Toggling
    const[activeKey, setActiveKey] = useState(null)

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
            
            // Update the form content state with data from the response
            setFormContent((prevContent) => ({
                ...prevContent,
                id: response.data.name || "",
                signal: response.data.signal || "",
                hazards: response.data.h_Stat || "",
                precautionary: response.data.p_Stat || "",
                supp_info: response.data.supp_info || "",
                pictograms: response.data.pictograms || "",
            }))

            // Expand the accordion
            setActiveKey("0")
        })
        .catch((error) => {
            console.error('Error submitting data:', error)
            setError(error.message)
        })
    }

    // Handle input changes
    const handleFormChange = (e) => {
        const { id, value} = e.target // 'id' to identify the field updated
        setFormContent((prevContent) => ({
            ...prevContent,
            [id]: value, // Updates the field dinamically
        }))
    }

    // Handle Form submit
    const handleFormSubmit = (e) => {
        e.preventDefault() // Prevent page reload
        console.log("Submitted form:", content)
        axios.post("http://localhost:3000/generate", content, {
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
                <Form.Control type="string" placeholder='Enter compound name' value={query} onChange={handleChange}/>
                <Form.Text>
                    Fetch compound safety data.
                </Form.Text>
               </Form.Group>
               <Button variant="primary" type="submit" onClick={handleSubmit}>
                Fetch
               </Button>
            </Form>
            
            <Accordion activeKey={activeKey}>
                <Accordion.Item eventKey="0">
                    <Accordion.Header>Label content</Accordion.Header>
                        <Accordion.Body>
                            <Form onSubmit={handleFormSubmit}>
                                <Form.Group className="mb-3" controlId="id">
                                    <Form.Label>Product Identifier</Form.Label>
                                    <Form.Control 
                                        type="text" 
                                        value={content.id} 
                                        onChange={handleFormChange}
                                    />
                                </Form.Group>

                                <Form.Group className="mb-3" controlId="signal">
                                    <Form.Label>Signal Word</Form.Label>
                                    <Form.Control 
                                        type="text" 
                                        value={content.signal} 
                                        onChange={handleFormChange}
                                    />
                                </Form.Group>

                                <Form.Group className="mb-3" controlId="hazards">
                                    <Form.Label>Hazard Statements</Form.Label>
                                    <Form.Control 
                                        type="text" 
                                        value={content.hazards} 
                                        onChange={handleFormChange}
                                        as="textarea"
                                        rows={6}
                                    />
                                </Form.Group>

                                <Form.Group className="mb-3" controlId="precautionary">
                                    <Form.Label>Precautionary Statements</Form.Label>
                                    <Form.Control 
                                        type="text" 
                                        value={content.precautionary} 
                                        onChange={handleFormChange}
                                        as="textarea"
                                        rows={12}
                                    />
                                </Form.Group>

                                <Form.Group className="mb-3" controlId="supp_info">
                                    <Form.Label>Supplier Information</Form.Label>
                                    <Form.Control 
                                        type="text" 
                                        value={content.supp_info} 
                                        onChange={handleFormChange}
                                    />
                                </Form.Group>

                                <Form.Group className="mb-3" controlId="pictograms">
                                    <Form.Label>Pictograms</Form.Label>
                                    <Form.Control 
                                        type="text" 
                                        value={content.pictograms} 
                                        onChange={handleFormChange}
                                    />
                                </Form.Group>

                                <Button variant="primary" type="submit">
                                    Generate Label
                                </Button>
                            </Form>
                        </Accordion.Body>
                </Accordion.Item>
            </Accordion>


        </div>
    );
}

export default CommandBar