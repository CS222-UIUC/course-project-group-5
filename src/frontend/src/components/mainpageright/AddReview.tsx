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
   ButtonGroup,
} from '@mui/material';

interface Props {
   apt: AptType | undefined;
   setReviews: Dispatch<SetStateAction<ReviewType[]>>;
   username: string;
   hasReview: boolean;
   handleAptChange: (apt: AptType) => void;
}

const baseURL = 'http://127.0.0.1:5000/main';
export default function AddReview({
   apt,
   setReviews,
   username,
   hasReview,
   handleAptChange,
}: Props) {
   const [text, setText] = useState<string>('');
   const [vote, setVote] = useState<number>(0);
   const queryApt = () => {
      axios({
         method: 'GET',
         url: `${baseURL}?search=True&aptId=${apt?.id}`,
      })
         .then((response) => {
            console.log(response);
            handleAptChange({
               id: response.data.apt_id,
               name: response.data.name,
               address: response.data.address,
               price_min: response.data.price_min,
               price_max: response.data.price_max,
               rating: response.data.rating,
            });
         })
         .catch((error) => {
            if (error.response) {
               console.log(error.response);
               console.log(error.response.status);
               console.log(error.response.headers);
            }
         });
   };
   const addReviewHandler = async (text: string, vote: number) => {
      // post review on submit
      const result = await axios.post(`${baseURL}`, {
         apt_id: apt?.id,
         username: username,
         comment: text,
         vote: vote,
      });
      queryApt();
      setReviews(result.data);
      console.log(result);
   };
   const deleteReview = () => {
      axios({
         method: 'POST',
         url: 'http://127.0.0.1:5000/main?delete=True',
         withCredentials: true,
         data: {
            apt_id: apt?.id,
            username: username,
         },
      })
         .then((response) => {
            console.log(response);
            setReviews(response.data);
            queryApt();
         })
         .catch((error) => {
            if (error.response) {
               console.log(error.response);
               console.log(error.response.status);
               console.log(error.response.headers);
            }
         });
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
               {hasReview === false && <FormLabel>Create a review</FormLabel>}
               {hasReview === true && (
                  <FormLabel>
                     You already reviewed this apartment, edit or delete it here
                  </FormLabel>
               )}
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
               <ButtonGroup variant="contained">
                  <Button type="submit" onClick={add}>
                     Submit
                  </Button>
                  {hasReview === true && (
                     <Button onClick={deleteReview}>Delete</Button>
                  )}
               </ButtonGroup>
            </Stack>
         </FormControl>
      </React.Fragment>
   );
}
