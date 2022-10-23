import './App.css';
import Formulario from "./components/form"


function App() {
  return (
    <div className="App">
      <header className="App-header">
      <div>
        <form action="https://flask-production-8840.up.railway.app/add" method="GET">
          <label>name:  </label>
          <input type="text" name="name" />
          <label>email:  </label>
          <input type="text" name="email" />
          <button type="submit">
            Submit
          </button>
        </form>
      </div>
      </header>
    </div>
  );
}

export default App;


