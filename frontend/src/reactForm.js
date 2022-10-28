import React, { Component } from 'react';

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
      alert('We will be in touch' + this.state.name + ": )");
      event.preventDefault();
    }
  
    render() {
      return (
        <form onSubmit={this.handleSubmit}>
          <label>
            name
            <input type="text" value={this.state.name} onChange={this.handleChangeName} />
          </label>
          <label>email
          <input type="text" value={this.state.email} onChange={this.handleChangeEmail} />
          </label>
                
          <input type="submit" value="Submit" />
        </form>
      );
    }
  }
  
  export default NameForm
  