import React, { useState, Dispatch, SetStateAction } from 'react';
import { ReviewType, AptType } from '../Types';
import axios from 'axios';
import {
   TextField,
   FormControl,
   FormControlLabel,
   FormLabel,
   RadioGroup,
   Button,
   Radio,
   Stack,
} from '@mui/material';

interface Props {
   apt: AptType | undefined;
   setReviews: Dispatch<SetStateAction<ReviewType[]>>;
   username: string;
}

const baseURL = 'http://127.0.0.1:5000/main';
export default function AddReview({ apt, setReviews, username }: Props) {
   const [text, setText] = useState<string>('');
   const [vote, setVote] = useState<number>(0);
   const addReviewHandler = async (text: string, vote: number) => {
      // post review on submit
      const result = await axios.post(`${baseURL}`, {
         apt_id: apt?.id,
         username: username,
         comment: text,
         vote: vote,
      });
      setReviews(result.data);
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
      <React.Fragment>
         {/* {error && <Alert variant="danger">{error}</Alert>} */}
         <FormControl className="mt-3 mb-3" onSubmit={add} key={apt?.id || 1}>
            <Stack spacing={2}>
               <FormLabel>Create a review</FormLabel>
               <TextField
                  label="Enter your reviews here"
                  onChange={(e) => setText(e.target.value)}
               ></TextField>
               <RadioGroup>
                  <FormControlLabel
                     value="upvote"
                     control={<Radio onChange={radioHandler} />}
                     label="Upvote"
                  />
                  <FormControlLabel
                     value="downvote"
                     control={<Radio onChange={radioHandler} />}
                     label="Downvote"
                  />
               </RadioGroup>
               <Button
                  type="submit"
                  variant="contained"
                  onClick={() => {
                     add();
                  }}
               >
                  Submit
               </Button>
            </Stack>
         </FormControl>
      </React.Fragment>
   );
}
