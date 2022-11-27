import { useEffect, useState } from 'react';
import axios from 'axios';
import { AptType } from '../Types';

const baseURL = 'http://127.0.0.1:5000/user';

export default function getReviewedApts(username: string) {
   // Get apts that username reviewed
   const [loading, setLoading] = useState(true);
   const [error, setError] = useState(false);
   const emptyarray: AptType[] = [];
   const [apartments, setApartments] = useState(emptyarray);

   useEffect(() => {
      setLoading(true);
      setError(false);
      const CancelToken = axios.CancelToken;
      const source = CancelToken.source();
      const timer = setTimeout(() => {
         const req = {
            is_get_liked: true,
            user_id: 1,
         };
         const json = JSON.stringify(req);
         axios({
            method: 'POST',
            url: `${baseURL}/${username}`,
            data: json,
            cancelToken: source.token,
         })
            .then((res) => {
               setApartments(() => {
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
                  return newApartments;
               });
            })
            .catch((e) => {
               if (axios.isCancel(e)) return;
               setError(true);
            });
      }, 700);
      return () => {
         clearTimeout(timer);
         source.cancel();
      };
   }, [username]);
   return { loading, error, apartments };
}
