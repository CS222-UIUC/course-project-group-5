import { useState, useEffect } from 'react';
import axios from 'axios';

function getApartments(query: string, pageNum: number, selected: string[]) {
   const [loading, setLoading] = useState(true);
   const [error, setError] = useState(false);
   const emptyarray: {
      // avoids linting warnings
      name: string;
      address: string;
      image: string;
      review: string;
      rating: number;
      price_min: string;
      price_max: string;
   }[] = [];
   const [apartments, setApartments] = useState(emptyarray);
   const [hasMore, setHasMore] = useState(false);

   useEffect(() => {
      // clears the apartments
      setApartments(emptyarray);
      pageNum = 1;
   }, [query, selected]);

   useEffect(() => {
      // GETs new apartments whenever a button is selected
      let limit = 2;
      if (query === '') {
         limit = 10;
      }
      setLoading(true);
      setError(false);
      const CancelToken = axios.CancelToken;
      const source = CancelToken.source();
      axios({
         method: 'GET', //http://localhost:3333/mockdata?q=${query}&_page=${pageNum}&_limit=2
         url: `http://localhost:3333/mockdata?q=${query}&_page=${pageNum}&_limit=${limit}`,
         cancelToken: source.token,
      })
         .then((res) => {
            const newApartments: {
               name: string;
               address: string;
               image: string;
               review: string;
               rating: number;
               price_min: string;
               price_max: string;
            }[] = [];
            for (let i = 0; i < res.data.length; i++) {
               if (res.data[i].name !== undefined) {
                  newApartments.push({
                     name: res.data[i].name,
                     address: res.data[i].address,
                     image: res.data[i].image,
                     review: res.data[i].review,
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
   }, [query, pageNum, selected]);

   return { loading, error, apartments, hasMore };
}

export default getApartments;
