import axios from "axios";
import SingleCard from "./SingleCard"

import React, { useEffect, useState } from "react";
import InfiniteScroll from "react-infinite-scroll-component";

export default function PreviewBlock(props: any) {
  return (
    <div style={{marginLeft: '30px'}}>
      <Scroll/>
    </div>
  );
};

/*
function ApartmentSearch(props: any) {

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [apartments, setApartments] = useState([]);
  const [hasMore, setHasMore] = useState(false);

  useEffect(() => {
    setApartments([]);
  }, []);

  useEffect(() => {
    setLoading(true);
    setError(false);
    let cancel = axios.CancelToken.source();
    axios({
      method: 'GET',
      url: 'http://localhost:3333/mockdata',
      cancelToken: new axios.CancelToken(c => cancel = c)
    }).then(res => {
      setApartments((prevApartments: ) => {
        return [...new Set([...prevApartments, ...res.data.docs.map(b => b.title)])];
      })
      setHasMore(res.data.length > 0);
      setLoading(false);
    }).catch(e => {
      if (axios.isCancel(e)) return;
      setError(true);
    })
    return () => cancel;
  }, [])

return { loading, error, apartments, hasMore }
}

*/

const Scroll = (props: any) => {
  const initialArray = [ // workaround until api works
    <SingleCard
    aptName="first"
    address="1"
    />,
    <SingleCard
    aptName="second"
    address="2"
    />,
    <SingleCard
    aptName="third"
    address="3"
    />,
    <SingleCard
    aptName="fourth"
    address="4"
    />
  ]
  const [items, setItems] = useState(initialArray);
  const [hasMore, setHasMore] = useState(true); // hasMore apartments
  const [name, setName] = useState("");
  const [components, setComponents] = useState(initialArray);

  const [count, setCount] = useState(0);

  useEffect(() => {
    axios.get('http://localhost:3333/mockdata')
      .then(response => {
        console.log(response.data);
        var newCards = [];
        const names = [];
        for (let i = 0; i < response.data.length; i++) {
          names.push(response.data[i].name);
          setName(response.data[i].name);
          newCards.push(SingleCard({address: response.data[i].name, aptName: response.data[i].address}));
        }
        //const cards = [SingleCard({address: name, aptName: "b"}) ];
        setComponents([...newCards]);
      })
      .then(function (error) {
        console.log(error);
      })
      .then(function () {});
  }, []);
  
  const fetchData = () => {
    console.log(count);
    setCount(count + 1);
    if (items.length >= 200) { // stop calling the api after 200 elements
      setHasMore(false);
      return;
    }
    setTimeout(() => {
      for (let i = 0; i < 2; i++) {
        console.log(components);
        setItems([...items, ...components]);
        components.shift();
      }
    }, 500);
  };

  return (
    <>
      <InfiniteScroll
      dataLength={items.length}
      next={fetchData}
      hasMore={hasMore}
      loader={<h4>Loading ...</h4>}
      endMessage={
        <p style={{ textAlign: "center" }}>
          <b>No more apartments</b>
        </p>
      }
      >
        {items.map((component, index) => (
          component
        ))}
      </InfiniteScroll>
    </>
  );
}
