import React, { Component } from 'react';
import axios from "axios";

class NameForm extends React.Component {
    constructor(props) {
      super(props);
      this.state = {name: '', email: ''};
  
      this.handleChangeName = this.handleChangeName.bind(this);
      this.handleChangeEmail = this.handleChangeEmail.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChangeName(event) {
      this.setState({name: event.target.value});
    }

    handleChangeEmail(event) {
        this.setState({email: event.target.value});
      }
  
    handleSubmit(event) {
      alert('We will be in touch with the address');
      event.preventDefault();
      let url = "https://www.capsula.ooo/add?name=" + this.state.name + "&email=" + this.state.email; 
      fetch(url)
        .then(response => response.json())
    }
  
    render() {
      return (
        <form onSubmit={this.handleSubmit}>
        <p>RSVP here</p>
          <label>
            name
            <input type="text" value={this.state.name} onChange={this.handleChangeName} />
          </label>
          <label>email
          <input type="text" value={this.state.email} onChange={this.handleChangeEmail} />
          </label>
                
          <input type="submit" value="Go" id="goButton"/>
        </form>
      );
    }
  }
  
  export default NameForm
  