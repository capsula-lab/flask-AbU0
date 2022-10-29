import "./App.css";
import Formulario from "./components/form";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import flyer from ".//flyer.jpg";
import "bootstrap/dist/css/bootstrap.css";
import Player from "./player";
import NameForm from "./reactForm";

function App() {
  return (
    <Row>
      <Col xs={12} s={12} m={6}>
        <img src={flyer} alt="Logo" />
      </Col>

      <Col>
        <Row>
          <Col></Col>
          <Col>
            <div id="form">
              <NameForm />
            </div>
          </Col>
          <Col>
            <Player />
          </Col>
        </Row>
      </Col>
    </Row>
  );
}

export default App;
