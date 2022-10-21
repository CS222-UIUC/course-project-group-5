import { useState, useEffect } from "react";
import axios from "axios";

function useSearchBook(query: string, pageNum: number) {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [apartments, setApartments] = useState(Array());
  const [hasMore, setHasMore] = useState(false);

  useEffect(() => {
    setApartments(Array());
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
      cancelToken: source.token
    }).then(res => {
      var newApartments: any[] = [];
      for (let i = 0; i < res.data.length; i++) {
        //console.log("name: " + " " + res.data[i].name);
        newApartments.push({
          'name': res.data[i].name,
          'company': res.data[i].company,
          'address': res.data[i].address,
          'image': res.data[i].image,
          'review': res.data[i].review,
          'priceLow': res.data[i].priceLow,
          'priceHigh': res.data[i].priceHigh
        });
      }
      setApartments(prevApartments => {
        return [...new Set([...prevApartments, ...newApartments])];
      });
      setHasMore(res.data.length > 0);
      setLoading(false);
    }).catch(e => {
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