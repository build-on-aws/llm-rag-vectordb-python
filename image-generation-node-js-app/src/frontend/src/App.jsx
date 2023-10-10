import axios from 'axios';
import React, { Component } from 'react';
import './App.css';

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Spinner from 'react-bootstrap/Spinner';
import Container from 'react-bootstrap/Container';
import Image from 'react-bootstrap/Image';

class App extends Component {
  state = {
    isLoadingVisible: false,
    val: '',
    imgSrc: '',
    style_preset: 'photographic'  // Default to photographic
  };

  showLoading = () => {
    this.setState({ isLoadingVisible: true });
  };

  hideLoading = () => {
    this.setState({ isLoadingVisible: false });
  };

  handleChange = (e) => {
    this.setState({
      style_preset: e.target.value
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    this.showLoading();

    const api = process.env.NODE_ENV === 'development' ? 'test/genai' : '<API-GW-ENDPOINT>'; // Replace with your API GW Endpoint
    const data = { 
      data: e.target.searchQuery.value,
      style_preset: this.state.style_preset 
    };

    axios({
      method: 'POST',
      data: JSON.stringify(data),
      headers: { 'Content-Type': 'application/json' },
      url: api,
    })
      .then((response) => {
        this.setState({ imgSrc: response.data.body });
        setTimeout(() => {
          this.hideLoading();
          this.setState({ val: '' });
        }, 500);
      })
      .catch((error) => {
        console.log(error);
      });
  };
  
  render() {
    return (
      <Container className='p-5 container' id='container' name='container'>
        <h1>Unleashing Machine Learning with Amazon Bedrock</h1>
        <Form onSubmit={this.handleSubmit}>
          <Form.Group className='mb-3' controlId='formBasicEmail'>
            <Form.Label className='form-label'>Your Words, Our Canvas: Enter Text to Create Image!</Form.Label>
            <Form.Control
              type='text'
              placeholder='Enter text to convert image'
              required
              autoFocus={true}
              name='searchQuery'
              controlId='searchQuery'
              defaultValue={this.state.val}
            />
            <Form.Text className='text-muted'>
              We'll sketch, stretch, and kvetch until your image is a fetching fetch
            </Form.Text>

            {/* Title for Radio buttons */}
            <p className="mt-3 font-weight-bold style-title">Select your style:</p>

            {/* Radio buttons horizontally aligned with some styling */}
            <div className="d-flex justify-content-between">
              <Form.Check
                inline
                type='radio'
                label='photographic'
                value='photographic'
                name='styleOptions'
                checked={this.state.style_preset === 'photographic'}
                onChange={this.handleChange}
                className='fancy-radio'
              />
              <Form.Check
                inline
                type='radio'
                label='digital-art'
                value='digital-art'
                name='styleOptions'
                checked={this.state.style_preset === 'digital-art'}
                onChange={this.handleChange}
                className='fancy-radio'
              />
              <Form.Check
                inline
                type='radio'
                label='cinematic'
                value='cinematic'
                name='styleOptions'
                checked={this.state.style_preset === 'cinematic'}
                onChange={this.handleChange}
                className='fancy-radio'
              />
            </div>

          </Form.Group>

          <Button variant='primary' type='submit' className='btn btn-primary btn-large centerButton'>
            Submit
          </Button>

          <Image id='myImage' className='img-fluid shadow-4' src={this.state.imgSrc} />
        </Form>

        {this.state.isLoadingVisible && (
          <div id='backdrop'>
            <Button variant='primary' disabled>
              <Spinner as='span' animation='grow' size='sm' role='status' aria-hidden='true' />
              Loading...
            </Button>
          </div>
        )}
      </Container>
    );
  }
}

export default App;
