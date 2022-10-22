import { useState, useEffect } from 'react';
import axios from 'axios';

function useSearchBook(query: string, pageNum: number) {
   const [loading, setLoading] = useState(true);
   const [error, setError] = useState(false);
   const array: {
      name: string;
      address: string;
      image: string;
      review: string;
      rating: number;
      price_min: string;
      price_max: string;
   }[] = [];
   const [apartments, setApartments] = useState(array);
   const [hasMore, setHasMore] = useState(false);

   useEffect(() => {
      setApartments(array);
   }, [query]);

   useEffect(() => {
      setLoading(true);
      setError(false);
      const CancelToken = axios.CancelToken;
      const source = CancelToken.source();
      axios({
         method: 'GET',
         url: `http://localhost:3333/mockdata?q=${query}&_page=${pageNum}&_limit=2`,
         params: { q: query, page: pageNum },
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
   }, [query, pageNum]);

   return { loading, error, apartments, hasMore };
}

export default useSearchBook;
