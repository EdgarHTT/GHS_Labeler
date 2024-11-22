import React from 'react'
import './App.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import CommandBar from './components/CommandBar.js';
import DisplayBar from './components/DisplayBar.js';

function App() {
  return (
    <Container fluid="xxl">
      <Row>
        <Col md={5} className="CommandBar">
          <CommandBar />
        </Col>
        <Col md={7}>
          <DisplayBar />
        </Col>
      </Row>
    </Container>
  )
}

export default App