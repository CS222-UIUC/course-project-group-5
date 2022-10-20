import { TextField } from "@mui/material";
import React, { useState, useRef, useCallback } from "react";
import SingleCard from "./SingleCard";
import useSearchApartment from "./useSearchApartment";

export default function Searching() {
  const [query, setQuery] = useState("");
  const [pageNum, setPageNum] = useState(1);
  const { loading, error, apartments, hasMore } = useSearchApartment(query, pageNum);
  console.log(apartments[0], apartments[1])
  const [press, setPress] = useState(false);
  const [amountFound, setAmountFound] = useState(0);

  const observer = useRef<any>();
  const lastBookElementRef = useCallback((node: any) => {
      if (loading) return;
      if (observer.current) observer.current.disconnect();
      observer.current = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting && hasMore) {
          setPageNum((prev) => prev + 1);
        }
      });
      if (node) observer.current.observe(node);
    },
    [loading, hasMore]
  );

  const handleChange = (e: any) => {
    setQuery(e.target.value);
    setPageNum(1);
    setPress(false);
  };

  const handlePress = (e: any) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        setPress(true);  
    } 
    setAmountFound(apartments.length);
  };

  const showCards = (e: any) => {
    for (let i = 0; i < apartments.length; i++) {

    }
  };

  return (
    <div className="App">
      <h1>Search For Apartments</h1>
      <div style={{display: 'flex', justifyContent: 'center'}}>
      <div className="search" style={{width: '800px'}}>
         <TextField
         id="outlined-basic"
         variant="outlined"
         fullWidth
         value={query || ''}
         label="Apartment Search"
         onKeyDown={handlePress} onChange={handleChange}
         />
      </div>
      <div>{press && amountFound == 0 && "None found"}</div>
      {press && apartments.map((apartments, i) => {
        if (apartments.length === i + 1) {
          return (
            <div key={i} ref={lastBookElementRef}>
              {apartments}
            </div>
          );
        } else {
                {apartments.map((i: any) => {
                    return <div> {apartments[i]} </div>
                })}

          //return <div>{SingleCard({address: apartments[0], aptName: "Hekllo"})}</div> 
        }
      })}
      <div>{press && loading && "Loading..."}</div>
      <div>{press && error && "Error..."}</div>
    </div>
    </div>
  );
}
