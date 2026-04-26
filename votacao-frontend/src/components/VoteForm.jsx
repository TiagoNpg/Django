import { useState } from "react";
import { Button, Form, FormGroup, Table, Label, Input } from "reactstrap";
import axios from "axios";
import moment from "moment";

function VoteForm({ options, question, toggle }) {
  const URL_OPTION = "http://localhost:8000/votacao/api/option/"; // (1)
  const URL_COMMENT = "http://localhost:8000/votacao/api/comments/";

  const [selectedOption, setSelectedOption] = useState(-1); // (2)
  const [author, setAuthor] = useState("");
  const [commentText, setCommentText] = useState("");

  const voteAndCloseModal = (event) => { // (3)
    event.preventDefault();

    const requests = [];

    if (selectedOption >= 0) {
      const option = { ...options[selectedOption] };
      option.votos++;

      requests.push(axios.put(URL_OPTION + option.id, option));
    }

    if (commentText.trim() !== "") {
      requests.push(axios.post(URL_COMMENT + question.id, {
        autor: author.trim() !== "" ? author.trim() : "Anónimo",
        comentario_texto: commentText.trim(),
      }));
    }

    Promise.all(requests).finally(() => {
      toggle();
    });
  };

  const optionChangeHandler = (event) => { // (4)
    const optionId = parseInt(event.target.value);
    setSelectedOption(optionId);
  };

  return (
    <>
      <Form onSubmit={voteAndCloseModal}> {/* (5) */}
        <FormGroup>
          <b>Texto:</b>
          <p>{question.questao_texto}</p>

          <b>Data de publicação:</b>
          <p>
            {moment(question.pub_data).format("YYYY-MM-DD HH:mm")}
          </p>
        </FormGroup>

        <FormGroup>
          <Label for="authorInput">Nome do autor</Label>
          <Input
            id="authorInput"
            type="text"
            value={author}
            onChange={(event) => setAuthor(event.target.value)}
            placeholder="Introduza o nome do autor"
          />
        </FormGroup>

        <FormGroup>
          <Label for="commentInput">Comentário</Label>
          <Input
            id="commentInput"
            type="textarea"
            value={commentText}
            onChange={(event) => setCommentText(event.target.value)}
            placeholder="Escreva um comentário sobre a questão"
          />
        </FormGroup>

        <FormGroup>
          <Table>
            <thead>
              <tr>
                <th align="left">Opção</th>
              </tr>
            </thead>
            <tbody>
              {options.map((o, index) => ( // (6)
                <tr key={o.id}>
                  <td align="left">
                    <FormGroup check>
                      <Label>
                        <input
                          type="radio"
                          name="react-radio"
                          checked={selectedOption === index}
                          value={index}
                          className="form-check-input"
                          onChange={optionChangeHandler}
                        />
                        {o.opcao_texto}
                      </Label>
                    </FormGroup>
                  </td>
                </tr>
              ))}
            </tbody>
          </Table>
        </FormGroup>

        <Button>Votar</Button> {/* (5) */}
      </Form>
    </>
  );
}

export default VoteForm;