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
      // gets new names whenever query changes
      const CancelToken = axios.CancelToken;
      const source = CancelToken.source();
      axios({
         method: 'GET',
         url: `http://127.0.0.1:5000/?search=${search}&searchQuery=${query}`,
         cancelToken: source.token,
         withCredentials: true,
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
