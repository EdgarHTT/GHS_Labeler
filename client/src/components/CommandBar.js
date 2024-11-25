import React, { useState } from 'react'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Accordion from 'react-bootstrap/Accordion'

function CommandBar() {
    return (
        <div>
            <Form>
               <Form.Group className="mb-3" 
               controlId="formCompoundName">
                <Form.Control type="query" placeholder='Enter compound name' />
                <Form.Text className="text-muted">
                    Fetch compound safety data.
                </Form.Text>
               </Form.Group>
               <Button variant="primary" type="submit">
                Fetch
               </Button>
            </Form>
            
            <Accordion defaultActiveKey="0">
                <Form>
                    <Accordion.Item eventKey="0">
                        <Accordion.Header>Compound safety data</Accordion.Header>
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
                            </Accordion.Body>
                    </Accordion.Item>
                </Form>
            </Accordion>


        </div>
    );
}

export default CommandBar