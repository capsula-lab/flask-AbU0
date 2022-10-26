import './App.css';
import Formulario from "./components/form"
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import flyer from './/flyer.png';
import 'bootstrap/dist/css/bootstrap.css';

function App() {
  return (
      <Row>
        <Col><img src={flyer} alt="Logo" /></Col>
        <Col>
        <Row>
          <Col>
          </Col>
          <Col>
            <form action="https://www.capsula.ooo/add" method="GET">
              <label>name</label>
              <input type="text" name="name" />
              <label>email</label>
              <input type="text" name="email" />
              <button type="submit">
                Go
              </button>
            </form>
          </Col>
          <Col>
          </Col>
        </Row>
          
        </Col>
      </Row>
  );
}

export default App;


