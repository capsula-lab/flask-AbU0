import React, { Component } from "react"
import axios from "axios"


class Formulario extends Component {
  constructor(props) {
    super(props)
  
    this.state = {
       name: "",
       email: "",
       response: ""
    }
  }

  handleNameChange = (event) => {
    this.setState({
      name: event.target.value
    })
  }
  handleMailChange = (event) => {
    this.setState({
      email: event.target.value
    })
  }

  handleSumbit = (event) => {
    event.preventDefault()
    alert(`${this.state.name}`)
    let url = "https://flask-production-8840.up.railway.app/api/" + this.state.name + "/" + this.state.email;
    axios.get(url).then(response => {
      console.log(response)
      this.setState(this.state.response)
    })
  }

    render() {
      return(
        <div>
          <form onSubmit={this.handleSubmit}>
            <label>
              Name:
              <input type="text" value={this.state.name} name="name" className="input" onChange={this.handleNameChange} />
            </label>
            <label>
              e-mail:
              <input type="text" value={this.state.email} name="e-mail" className="input" onChange={this.handleMailChange} />
            </label>
            <button onClick={this.handleSubmit.bind} type="submit" value="Submit"></button>
          </form>
          <p>{this.state.response}</p>
        </div>
      )
    }
}

export default Formulario