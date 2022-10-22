import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          loading...
        </p>
        <form>
  <label>
    Name:
    <input type="text" name="name" />
  </label>
  <label>
    e-mail:
    <input type="text" name="e-mail" />
  </label>
  <input type="submit" value="Submit" />
</form>
      </header>
    </div>
  );
}

export default App;
