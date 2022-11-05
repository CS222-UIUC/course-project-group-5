import { useState, useEffect } from 'react';
import axios from 'axios';

function getApartments(
   query: string,
   pageNum: number,
   priceSort: string[],
   ratingSort: string[]
) {
   const [loading, setLoading] = useState(true);
   const [error, setError] = useState(false);
   const emptyarray: {
      // avoids linting warnings
      apt_id: number;
      name: string;
      address: string;
      rating: number;
      price_min: number;
      price_max: number;
   }[] = [];
   const [apartments, setApartments] = useState(emptyarray);
   const [hasMore, setHasMore] = useState(false);

   useEffect(() => {
      // clears the apartments
      setApartments(emptyarray);
      pageNum = 1;
   }, [priceSort, ratingSort]);

   useEffect(() => {
      // gets new apartments on initial load and when a button is selected
      let limit = 2;
      if (query === '') {
         limit = 10;
      }
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
      axios({
         // http://127.0.0.1:5000/?populate=${populate}&priceSort=${priceNum}&ratingSort=${ratingNum}&numApts=${limit}&_page=${pageNum}
         method: 'GET', //http://localhost:3333/mockdata?q=${query}&_page=${pageNum}&_limit=2
         url: `http://127.0.0.1:5000/?populate=${populate}&priceSort=${priceNum}&ratingSort=${ratingNum}&numApts=${limit}`,
         cancelToken: source.token,
      })
         .then((res) => {
            const newApartments: {
               apt_id: number;
               name: string;
               address: string;
               rating: number;
               price_min: number;
               price_max: number;
            }[] = [];
            for (let i = 0; i < res.data.length; i++) {
               if (res.data[i].name !== undefined && pageNum == 1) {
                  newApartments.push({
                     apt_id: res.data[i].apt_id,
                     name: res.data[i].name,
                     address: res.data[i].address,
                     rating: res.data[i].rating,
                     price_min: res.data[i].price_min,
                     price_max: res.data[i].price_max,
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
      return () => {
         source.cancel();
      };
   }, [pageNum, priceSort, ratingSort]);

   return { loading, error, apartments, hasMore };
}

function convertPriceSort(sort: string[]) {
   if (sort.includes('low-high')) {
      return -1;
   } else if (sort.includes('high-low')) {
      return 1;
   } else {
      return 0;
   }
}

function convertRatingSort(sort: string[]) {
   if (sort.includes('least popular')) {
      return -1;
   } else if (sort.includes('most popular')) {
      return 1;
   } else {
      return 0;
   }
}

export default getApartments;
