import React from 'react';
import ReviewCard from './ReviewCard';
import { ReviewType } from '../Types';

interface Props {
   reviews: ReviewType[];
}
const ReviewsList = ({ reviews }: Props) => {
   if (reviews.length === 0) {
      return (
         <div>
            <h3>No comment yet. Write your first comment</h3>
         </div>
      );
   } else {
      return (
         <div className="container-fluid">
            <h3 className="text-center">Comments</h3>
            <hr></hr>
            {reviews.map((review, i) => (
               <ReviewCard
                  key={i}
                  username={review.username}
                  date={review.date}
                  comment={review.comment}
                  vote={review.vote}
               />
            ))}
         </div>
      );
   }
};

export default ReviewsList;
