import { Button, Form, FormGroup, Table } from "reactstrap";
import moment from "moment";

function DetailData({ options, comments, question, toggle }) { // (1)
  const closeModal = (e) => { // (2)
    e.preventDefault();
    toggle();
  };

  return (
    <Form onSubmit={closeModal}> {/* (3) */}
      <FormGroup>
        <b>Texto:</b>
        <p>{question.questao_texto}</p>

        <b>Data de publicação:</b>
        <p>
          {moment(question.pub_data).format("YYYY-MM-DD HH:mm")}
        </p> {/* (4) */}
      </FormGroup>

      <FormGroup>
        <Table>
          <thead>
            <tr>
              <th style={{ textAlign: "left" }}>Opção</th>
              <th style={{ textAlign: "right" }}>Votos</th>
            </tr>
          </thead>
          <tbody>
            {options.map((o) => ( // (5)
              <tr key={o.id}>
                <td style={{ textAlign: "left" }}>{o.opcao_texto}</td>
                <td style={{ textAlign: "right" }}>{o.votos}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </FormGroup>

      <FormGroup>
        <b>Comentários:</b>
        <Table>
          <thead>
            <tr>
              <th style={{ textAlign: "left" }}>Autor</th>
              <th style={{ textAlign: "left" }}>Comentário</th>
            </tr>
          </thead>
          <tbody>
            {comments.length === 0 ? (
              <tr>
                <td colSpan="2" style={{ textAlign: "left" }}>Sem comentários.</td>
              </tr>
            ) : (
              comments.map((comment) => (
                <tr key={comment.id}>
                  <td style={{ textAlign: "left" }}>{comment.autor}</td>
                  <td style={{ textAlign: "left" }}>{comment.comentario_texto}</td>
                </tr>
              ))
            )}
          </tbody>
        </Table>
      </FormGroup>

      <Button>Fechar</Button> {/* (3) */}
    </Form>
  );
}

export default DetailData;