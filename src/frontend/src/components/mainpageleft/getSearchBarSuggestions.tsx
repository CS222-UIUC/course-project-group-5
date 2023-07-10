import { useState, useEffect } from 'react';
import axios from 'axios';
import { AptType } from '../Types';

export default function getSuggestions(query: string, search: boolean) {
   const [apts, setApts] = useState<AptType[]>([]);

   useEffect(() => {
      // clears the names
      setApts([]);
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
            const newApts: AptType[] = [];
            for (let i = 0; i < res.data.length; i++) {
               if (res.data[i].name !== undefined) {
                  newApts.push({
                     id: res.data[i].apt_id,
                     name: res.data[i].name,
                     address: res.data[i].address,
                     price_min: res.data[i].price_min,
                     price_max: res.data[i].price_max,
                     rating: res.data[i].rating,
                  });
               }
            }
            setApts(newApts);
         })
         .catch((e) => {
            if (axios.isCancel(e)) return;
         });
      return () => {
         source.cancel();
      };
   }, [query]);

   return { apts };
}
