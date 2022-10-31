import {
   Autocomplete,
   Stack,
   TextField,
   ToggleButton,
   ToggleButtonGroup,
} from '@mui/material';
import React, { useState, useRef, useCallback } from 'react';
import SingleCard from './SingleCard';
import data from '../staticdata.json';
import getApartments from './getApartments';
import { useSearchParams } from 'react-router-dom';
import './SearchBarStyles.css';

export default function Searching() {
   const [query, setQuery] = useState('');
   const [searchParams, setSearchParams] = useSearchParams();
   const [pageNum, setPageNum] = useState(1);
   const emptyarray: string[] = [];
   const [selected, setSelected] = useState(emptyarray);
   const { loading, error, apartments, hasMore } = getApartments(
      query,
      pageNum,
      selected
   );

   const observer = useRef<IntersectionObserver | null>(null);
   // prevents the infinite scroll from triggering forever
   const lastBookElementRef = useCallback(
      (node: HTMLDivElement) => {
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

   const handleSubmit = (
      event: React.SyntheticEvent<Element, Event>,
      value: string
   ) => {
      event.preventDefault();
      setQuery(value);
      if (value === '') {
         searchParams.delete('searchQuery');
         searchParams.set('search', 'False');
      } else {
         searchParams.set('searchQuery', value);
         searchParams.set('search', 'True');
      }
      searchParams.set('numApts', '10');
      setSearchParams(searchParams);
   };

   const handleToggle = (
      event: React.SyntheticEvent<Element, Event>,
      newSelected: string[]
   ) => {
      // prevents "high-low" and "low-high" from being selected at the same time
      if (
         newSelected.includes('low-high') &&
         newSelected.includes('high-low')
      ) {
         if (newSelected.at(0) !== 'most popular') {
            newSelected.shift();
         } else {
            newSelected.splice(1, 1);
         }
      }
      setSelected(newSelected);
      // sets URL
      if (newSelected.includes('low-high')) {
         searchParams.set('priceSort', '-1');
      } else if (newSelected.includes('high-low')) {
         searchParams.set('priceSort', '1');
      } else {
         searchParams.delete('priceSort');
      }
      if (newSelected.includes('most popular')) {
         searchParams.set('ratingSort', '1');
      } else {
         searchParams.delete('ratingSort');
      }
      setSearchParams(searchParams);
   };

   return (
      <div className="App">
         <div>
            <div style={{ display: 'flex', justifyContent: 'center' }}></div>
            <h1>Apartment Search</h1>
            <div className="search">
               <Stack spacing={2} sx={{ width: 500 }}>
                  <Autocomplete
                     id="free-solo-demo"
                     freeSolo
                     onInputChange={handleSubmit}
                     options={data.map((option) => option.name)}
                     renderInput={(params) => (
                        <TextField {...params} label="Search" />
                     )}
                  />
               </Stack>
            </div>
            <br />
            <ToggleButtonGroup
               color="primary"
               value={selected}
               onChange={handleToggle}
               aria-label="Platform"
            >
               <ToggleButton value="low-high">Low-High</ToggleButton>
               <ToggleButton value="high-low">High-Low</ToggleButton>
               <ToggleButton value="most popular">Most Popular</ToggleButton>
            </ToggleButtonGroup>
            <br />
            <br />
            <br />
            <div>
               {apartments.length === 0 && !loading && 'None found'}
            </div>
            <div>
               {apartments.map((apartment, i) => {
                  if (apartments.length === i + 1) {
                     return (
                        // handles last element
                        <div key={i} ref={lastBookElementRef}>
                           <SingleCard {...apartment} key={i} />
                        </div>
                     );
                  } else {
                     return (
                        <div key={i}>
                           <SingleCard {...apartment} key={i} />
                        </div>
                     );
                  }
               })}
            </div>
            <div>{loading && 'Loading...'}</div>
            <div>{error && 'Error...'}</div>
         </div>
      </div>
   );
}
