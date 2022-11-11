import { useState, useEffect } from 'react';
import axios from 'axios';
import { AptType } from '../Types';

function getApartments(priceSort: string, ratingSort: string, id: number) {
   const [loading, setLoading] = useState(true);
   const [error, setError] = useState(false);
   const emptyarray: AptType[] = [];
   const [apartments, setApartments] = useState(emptyarray);
   const [hasMore, setHasMore] = useState(false);

   useEffect(() => {
      // clears the apartments
      setApartments(emptyarray);
   }, [priceSort, ratingSort]);

   useEffect(() => {
      // gets new apartments on initial load, when a button is selected, and when the user scrolls to the bottom
      const priceNum = convertPriceSort(priceSort);
      const ratingNum = convertRatingSort(ratingSort);
      let populate = 'True';
      if (priceNum === 0 && ratingNum === 0) {
         populate = 'False';
      }
      setLoading(true);
      setError(false);
      const CancelToken = axios.CancelToken;
      const source = CancelToken.source();
      const timer = setTimeout(() => {
         // creates the illusion that page is loading
         axios({
            method: 'GET',
            url: `http://127.0.0.1:5000/?populate=${populate}&priceSort=${priceNum}&ratingSort=${ratingNum}&numApts=5&aptId=${id}`,
            cancelToken: source.token,
         })
            .then((res) => {
               const newApartments: AptType[] = [];
               for (let i = 0; i < res.data.length; i++) {
                  if (res.data[i].name !== undefined) {
                     newApartments.push({
                        // this is necessary; pushing res.data[i] does not work
                        id: res.data[i].apt_id,
                        name: res.data[i].name,
                        address: res.data[i].address,
                        price_min: res.data[i].price_min,
                        price_max: res.data[i].price_max,
                        votes: res.data[i].votes,
                     });
                  }
               }
               setApartments((prevApartments) => {
                  return [...new Set([...prevApartments, ...newApartments])];
               });
               setHasMore(res.data.length > 0);
               setLoading(false);
            })
            .catch((e) => {
               if (axios.isCancel(e)) return;
               setError(true);
            });
      }, 900);
      return () => {
         clearTimeout(timer);
         source.cancel();
      };
   }, [id, priceSort, ratingSort]);

   return { loading, error, apartments, hasMore };
}

function convertPriceSort(sort: string) {
   if (sort === 'low-high') {
      return -1;
   } else if (sort === 'high-low') {
      return 1;
   } else {
      return 0;
   }
}

function convertRatingSort(sort: string) {
   if (sort === 'least popular') {
      return -1;
   } else if (sort === 'most popular') {
      return 1;
   } else {
      return 0;
   }
}

export default getApartments;
