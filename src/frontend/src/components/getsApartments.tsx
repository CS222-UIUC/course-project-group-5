import { useState, useEffect, useRef } from 'react';
import axios from 'axios';

function useSearchApartment(
   query: string,
   pageNum: number,
   press: boolean,
   selected: string[]
) {
   const [loading, setLoading] = useState(true);
   const [error, setError] = useState(false);
   const array: {
      // avoids linting warnings
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
      // clears the apartments when "enter" is pressed or any button is selected
      setApartments(array);
   }, [press, selected]);

   /* 
   All useEffect functions are performed on page load and whenever the properties 
   in the dependency array changes. For example, in the useEffect above, the 
   dependency array is [press, selected], so whenever "press" or "selected" change, 
   the useEffect is triggered.
   */

   const isInitialMount = useRef<boolean>(true); // this prevents useEffect from triggering everytime query is changed
   useEffect(() => {
      // populates the page on initial page load and when the search bar is ever empty
      if (isInitialMount.current == true || query === '') {
         isInitialMount.current = false;
         setLoading(true);
         setError(false);
         const CancelToken = axios.CancelToken;
         const source = CancelToken.source();
         axios({
            method: 'GET', // the "_limit=10" below is how many will be taken from the url
            url: `http://localhost:3333/mockdata?q=${query}&_page=${pageNum}&_limit=10`,
            cancelToken: source.token,
         })
            .then((res) => {
               const newApartments: {
                  // avoids linting warnings
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
                  // concats new apartments to the array
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
      }
   }, [query]);

   const isInitialPress = useRef<boolean>(true);
   useEffect(() => {
      // GETs new apartments whenever enter is pressed or a button is selected
      if ((pageNum === 1 && press) || !isInitialPress.current) {
         isInitialPress.current = false;
         setLoading(true);
         setError(false);
         const CancelToken = axios.CancelToken;
         const source = CancelToken.source();
         axios({
            method: 'GET', //http://localhost:3333/mockdata?q=${query}&_page=${pageNum}&_limit=2
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
      }
   }, [pageNum, press, selected]); // there's a bug here since pageNum will be triggered at the wrong time

   return { loading, error, apartments, hasMore };
}

export default useSearchApartment;
