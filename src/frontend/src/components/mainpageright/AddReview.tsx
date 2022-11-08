import React, { useState } from 'react';
import { Button, Form } from 'react-bootstrap';
import axios from 'axios';

const baseURL = 'http://127.0.0.1:5000/main';
export default function AddReview() {
   const [text, setText] = useState<string>('');
   const [vote, setVote] = useState<number>(0);
   const addReviewHandler = async (text: string, vote: number) => {
      // post review on submit
      const result = await axios.post(`${baseURL}`, {
         apt_id: 2,
         username: 'Zongxian',
         comment: text,
         vote: vote,
      });
      console.log(result);
   };
   const radioHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
      console.log(typeof event.target.value);
      // set the vote
      if (event.target.value === 'upvote') {
         setVote(1);
      } else if (event.target.value === 'downvote') {
         setVote(-1);
      }
   };
   const add = () => {
      if (text === '' || vote === 0) {
         // alert on error
         alert('All fields are mandatory!');
         return;
      }
      addReviewHandler(text, vote);
   };
   return (
      <div>
         {/* {error && <Alert variant="danger">{error}</Alert>} */}
         <hr></hr>
         <Form className="mt-3 mb-3" onSubmit={add}>
            <Form.Group className="mb-3 text-center" controlId="formBasicText">
               <Form.Label>Create a Review</Form.Label>
               <Form.Control
                  placeholder="Enter your reviews here"
                  as="textarea"
                  rows={5}
                  onChange={(e) => setText(e.target.value)}
               />
            </Form.Group>
            <div className="mb-3">
               <div className="form-check form-check-inline ">
                  <input
                     name="group1"
                     type="radio"
                     value="upvote"
                     id="inline-radio-1"
                     className="form-check-input"
                     onChange={radioHandler}
                  />
                  <label
                     title=""
                     htmlFor="inline-radio-1"
                     className="form-check-label"
                  >
                     upvote
                  </label>
               </div>
               <div className="form-check form-check-inline">
                  <input
                     name="group1"
                     type="radio"
                     value="downvote"
                     id="inline-radio-2"
                     className="form-check-input"
                     onChange={radioHandler}
                  />
                  <label
                     title=""
                     htmlFor="inline-radio-2"
                     className="form-check-label"
                  >
                     downvote
                  </label>
               </div>
            </div>
            <Button type="submit" variant="primary">
               Submit
            </Button>
         </Form>
      </div>
   );
}
