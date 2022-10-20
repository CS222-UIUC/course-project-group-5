import React, { useState, useEffect } from "react";
import axios from "axios";

function useSearchBook(query: string, pageNum: number) {
const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [books, setBooks] = useState(Array());
  const [apartments, setApartments] = useState(Array());
  const [hasMore, setHasMore] = useState(false);
  useEffect(() => {
    //setBooks(Array());
    setApartments(Array());
  }, [query]);

  useEffect(() => {
    setLoading(true);
    setError(false);
    const CancelToken = axios.CancelToken;
    const source = CancelToken.source();
    axios({
      method: 'GET',
      url: `http://localhost:3333/mockdata?q=${query}`,
      params: { q: query },
      //cancelToken: new axios.CancelToken(c => cancel = c)
      cancelToken: source.token
    }).then(res => {
      //setBooks(prevBooks => {
      //  return [...new Set([...prevBooks, ...res.data.map((b: any) => b.name)])];
      //})
      var array: any[] = [];
      for (let i = 0; i < res.data.length; i++) {
        console.log("name: " + " " + res.data[i].name);
        array.push({'name': res.data[i].name, 'address': res.data[i].address});
      }
      const obj = {'name': res.data.name, 'address': res.data.address};
      setApartments(prevApartments => {
        //return [...new Set([...prevApartments, ...res.data.map((b: any) => b.name)])];
        //return [...new Set([...prevApartments, {...res.data.map((b: any) => b.name), 
        //    ...res.data.map((b: any) => b.address)}])];
        return [...new Set([...prevApartments, ...array])];
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
  }, [query]);

  return { loading, error, apartments, hasMore };
}

export default useSearchBook;
/*
  useEffect(() => {
    setBooks(Array());
  }, [query]);

  useEffect(() => {
    const CancelToken = axios.CancelToken;
    let cancel = CancelToken.source();
    const controller = new AbortController();
    setIsLoading(true);
    setError(false);

    axios.get('http://localhost:3333/mockdata', {
        //cancelToken: new axios.CancelToken((c) => (cancel.cancel = c))
        cancelToken: cancel.token,
        signal: controller.signal
      }).then((res) => {
        console.log("HELLO");
        console.log(res.data + " " + res.data.name);
        setBooks((prev: any) => {
          return [...new Set([...prev, ...res.data.map((d: any) => d.name)])];
        });
        setHasMore(res.data.length > 0);
        setIsLoading(false);
      })
      .catch(function (thrown) {
        console.log(thrown);
        if (axios.isCancel(thrown)) {
          console.log('Request canceled', thrown.message);
        } else {
          // handle error
        }
      });
      /*.then((res) => {
        console.log(res.data + " " + res.data.name);
        setBooks((prev: any) => {
          return [...new Set([...prev, ...res.data.map((d: any) => d.name)])];
        });
        setHasMore(res.data.length > 0);
        setIsLoading(false);
      })
      .catch((err) => {
        console.log(err);
        if (axios.isCancel(err)) return;
        setError(err);
      });

    return () => controller.abort();
    controller.abort();
  }, [query, pageNum]);

  return { isLoading, error, books, hasMore };
}

export default useSearchBook;
*/