import React from 'react'
import './App.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import CommandBar from './CommandBar/CommandBar';
import DisplayBar from './DisplayBar/DisplayBar';

function App() {
  return (
    <Container>
      <Row>
        <Col sm={5}>
          <CommandBar />
        </Col>
        <Col sm={6}>
          <DisplayBar />
        </Col>
      </Row>
    </Container>
  )
}

export default App