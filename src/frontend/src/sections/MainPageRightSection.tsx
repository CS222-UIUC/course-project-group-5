import React, { useState, useEffect } from 'react';
import ReviewsList from '../components/ReviewsList';
import AddReview from '../components/AddReview';
import ImagesGallery from '../components/ImagesGallery';
import { ReviewType, AptType } from '../components/Types';
import { AptInfo } from '../components/AptInfo';
import axios from 'axios';

const baseURL = 'http://127.0.0.1:5000/main';
interface apt {
   apt: AptType | undefined; // in case of null
}
function RightSection({ apt }: apt) {
   const [reviews, setReviews] = useState<ReviewType[]>([]);
   const [pics, setPics] = useState<string[]>([
      'https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled.png',
   ]);
   // const [aptInfo, setAptInfo] = useState<AptType>({
   //    id: -1,
   //    name: 'Apartment Name',
   //    address: 'Apartment Address',
   //    price_min: 0,
   //    price_max: 9999,
   //    votes: -1,
   // });
   // setAptInfo(apt);
   const retrieveReviews = async () => {
      const response = await axios.get(
         `${baseURL}?review=True&aptId=${apt?.id || 1}`
      );
      console.log(response.data);
      return response.data;
   };
   const retrievePics = async () => {
      const response = await axios.get(
         `${baseURL}?pictures=True&aptId=${apt?.id || 1}`
      );
      console.log(response.data);
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
      <div className="container">
         <ImagesGallery pics={pics} />
         <AptInfo apt={apt} />
         <AddReview />
         <ReviewsList reviews={reviews} />
      </div>
   );
}

export default RightSection;
