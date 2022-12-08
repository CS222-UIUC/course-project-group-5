import React, { useState, useEffect } from 'react';
import ReviewsList from '../components/mainpageright/ReviewsList';
import AddReview from '../components/mainpageright/AddReview';
import ImagesGallery from '../components/mainpageright/ImagesGallery';
import { ReviewType, AptType } from '../components/Types';
import { AptInfo } from '../components/mainpageright/AptInfo';
import axios from 'axios';
import { Stack, Divider } from '@mui/material';

const baseURL = 'http://127.0.0.1:5000/main';
interface apt {
   apt: AptType | undefined; // in case of null
   logged: boolean;
   username: string;
   handleAptChange: (apt: AptType) => void;
}
function RightSection({ apt, logged, username, handleAptChange }: apt) {
   const [reviews, setReviews] = useState<ReviewType[]>([]);
   const [pics, setPics] = useState<string[]>([
      'https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled.png',
   ]);
   const [hasReview, setHasReview] = useState(false);
   function checkHasReview() {
      axios({
         url: `${baseURL}?review=True&aptId=${apt?.id || 1}&checkReview=True`,
         withCredentials: true,
      })
         .then((response) => {
            console.log(response);
            setHasReview(true);
         })
         .catch((error) => {
            if (error.response) {
               console.log(error.response);
               console.log(error.response.status);
               console.log(error.response.headers);
               setHasReview(false);
            }
         });
   }
   useEffect(() => {
      checkHasReview();
   }, [apt]);
   const retrieveReviews = async () => {
      const response = await axios.get(
         `${baseURL}?review=True&aptId=${apt?.id || 1}`
      );
      return response.data;
   };
   const retrievePics = async () => {
      const response = await axios.get(
         `${baseURL}?pictures=True&aptId=${apt?.id || 1}`
      );
      return response.data;
   };
   useEffect(() => {
      const getAllPics = async () => {
         const allPics = await retrievePics();
         if (allPics) setPics(allPics);
      };
      getAllPics();
   }, [apt]);
   useEffect(() => {
      const getAllReviews = async () => {
         const allReviews = await retrieveReviews();
         if (allReviews) setReviews(allReviews);
      };
      getAllReviews();
   }, [apt]);
   return (
      <React.Fragment>
         {/* A column of every element on the right half */}
         <Stack spacing={3}>
            <ImagesGallery pics={pics} />
            <AptInfo apt={apt} />
            {logged === true && (
               <React.Fragment>
                  <Divider
                     sx={{ borderBottomWidth: 3, bgcolor: 'secondary.dark' }}
                  />
                  <AddReview
                     apt={apt}
                     setReviews={setReviews}
                     username={username}
                     hasReview={hasReview}
                     handleAptChange={handleAptChange}
                  />
               </React.Fragment>
            )}
            <Divider sx={{ borderBottomWidth: 3, bgcolor: 'secondary.dark' }} />
            <ReviewsList reviews={reviews} />
         </Stack>
      </React.Fragment>
   );
}

export default RightSection;
