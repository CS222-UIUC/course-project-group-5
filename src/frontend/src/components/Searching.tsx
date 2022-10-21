import { TextField, ToggleButton, ToggleButtonGroup } from "@mui/material";
import axios from "axios";
import React, { useState, useRef, useCallback } from "react";
import SingleCard from "./SingleCard";
import useSearchApartment from "./useSearchApartment";

export default function Searching() {
  const [query, setQuery] = useState("");
  const [pageNum, setPageNum] = useState(1);
  const { loading, error, apartments, hasMore } = useSearchApartment(query, pageNum);
  console.log(apartments);

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
    if (e.key === "Enter") {
        e.preventDefault();
        setPress(true);
        handlePost;
        setAmountFound(apartments.length);
    } 
    
  };

  function handlePost(query: string) {
    axios({
        method: 'post',
        url: 'http://localhost:3333/mockdata', // need mainpage.py url
        data: {
            q: query
        },
    })
    .then((response) => {
        //console.log(response);
    })
    .catch((error) => {
        if (error.response) {
            console.log(error.response);
            console.log(error.response.status);
            console.log(error.response.headers);
        }
    });
}

const [alignment, setAlignment] = React.useState(Array());

  const handleToggle = (
    event: React.MouseEvent<HTMLElement>,
    newAlignment: string[],
  ) => {
    setAlignment(newAlignment);
  };

  return (
    <div className="App">
        <h1>Search For Apartments</h1>
        <div>
        <div style={{display: 'flex', justifyContent: 'center'}}>
            <div className="search" style={{width: '800px'}}>
            <TextField
            id="outlined-basic"
            variant="outlined"
            fullWidth
            value={query || ''}
            label="Apartment Search"
            onKeyDown={handlePress} 
            onChange={handleChange}
            />
            </div>
            </div>
            {/*<div>{press && amountFound === 0 && !loading && "None found"}</div>*/}
            <br/>
            <ToggleButtonGroup
              color="primary"
              value={alignment}
              onChange={handleToggle}
              aria-label="Platform"
            >
              <ToggleButton value="price">Price</ToggleButton>
              <ToggleButton value="android">Android</ToggleButton>
              <ToggleButton value="ios">iOS</ToggleButton>
            </ToggleButtonGroup>
            <br/>
            <br/>
            <br/>
            <div>
                {press && apartments.map((apartment, i) => {
                  console.log(apartment.image);
                if (apartments.length === i + 1) {
                    return (
                        <div key={i} ref={lastBookElementRef}>
                            <SingleCard {...apartment} key={i} />
                        </div>
                    );
                } else {
                    return (
                        <div key={i}>
                            <SingleCard {...apartment} key={i}/>
                        </div>
                    );
                }
            })}
            </div>
            <div>{press && loading && "Loading..."}</div>
            <div>{press && error && "Error..."}</div>
        </div>
    </div>
  );
}