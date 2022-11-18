import React, { MouseEventHandler } from 'react';
import ReviewCard from './ReviewCard';
import { ReviewType } from '../Types';
import axios from 'axios';
const baseURL = 'http://127.0.0.1:5000/main?delete=True';
interface Props {
   reviews: ReviewType[];
}
const ReviewsList = ({ reviews }: Props) => {
   const handleDelete = async (apt_id: number, username: string) => {
      const result = await axios.post(`${baseURL}`, {
         apt_id: apt_id,
         username: username,
      });
      console.log(result);
   };
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
                  apt_id={review.apt_id}
                  username={review.username}
                  date={review.date}
                  comment={review.comment}
                  vote={review.vote}
                  // delete={handleDelete}
               />
            ))}
         </div>
      );
   }
};

export default ReviewsList;
