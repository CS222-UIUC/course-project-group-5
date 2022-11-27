import React from 'react';
import ReviewCard from './ReviewCard';
import { ReviewType } from '../Types';
import { Box, Typography, Stack } from '@mui/material';
interface Props {
   reviews: ReviewType[];
}
const ReviewsList = ({ reviews }: Props) => {
   return (
      <React.Fragment>
         {reviews.length === 0 && (
            <Box display="flex" justifyContent="center">
               <Typography variant="h5">
                  No comment yet. Write your first comment
               </Typography>
            </Box>
         )}
         {reviews.length !== 0 && (
            <Stack spacing={1}>
               <Box display="flex" justifyContent="center">
                  <Typography variant="h5">Comments</Typography>
               </Box>
               {reviews.map((review, i) => (
                  <ReviewCard
                     key={i}
                     username={review.username}
                     date={review.date}
                     comment={review.comment}
                     vote={review.vote}
                  />
               ))}
            </Stack>
         )}
      </React.Fragment>
   );
};

export default ReviewsList;
