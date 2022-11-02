import { useState, useEffect } from 'react';
import axios from 'axios';

export default function getSuggestions(query: string, search: boolean) {
   const emptyarray: {
      name: string;
   }[] = [];
   const [names, setNames] = useState(emptyarray);

   useEffect(() => {
      // clears the names
      setNames(emptyarray);
   }, [query]);

   useEffect(() => {
      // GETs new names whenever a button is selected
      const CancelToken = axios.CancelToken;
      const source = CancelToken.source();
      axios({
         method: 'GET',
         url: `http://localhost:3333/mockdata?search=${search}&searchQuery=${query}`,
         cancelToken: source.token,
      })
         .then((res) => {
            const newNames: {
               name: string;
            }[] = [];
            for (let i = 0; i < res.data.length; i++) {
               if (res.data[i].name !== undefined) {
                  newNames.push({
                     name: res.data[i].name,
                  });
               }
            }
            //setNames((prevNames) => {
            //   return [...new Set([...prevApartments, ...newApartments])];
            //});
            setNames(newNames);
         })
         .catch((e) => {
            if (axios.isCancel(e)) return;
         });
      return () => {
         source.cancel();
      };
   }, [query]);

   return { names };
}
