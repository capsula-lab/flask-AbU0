import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <form>
  <label>
    Name:
    <input type="text" name="name" className="input" />
  </label>
  <label>
    e-mail:
    <input type="text" name="e-mail" className="input" />
  </label>
  <input type="submit" value="Submit" />
</form>
      </header>
    </div>
  );
}

export default App;
