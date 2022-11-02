import { ToggleButton, ToggleButtonGroup } from '@mui/material';
import React, { useState, useRef, useCallback } from 'react';
import SingleCard from './SingleCard';
import { useSearchParams } from 'react-router-dom';
import './SearchBarStyles.css';
import getApartments from './getApts';

export default function Populate() {
   // eslint-disable-next-line
   const [query, setQuery] = useState('');
   const [searchParams, setSearchParams] = useSearchParams();
   const [pageNum, setPageNum] = useState(1);
   // eslint-disable-next-line
   const [id, setId] = useState(-1);
   const emptyarray: string[] = [];
   const [selected, setSelected] = useState(emptyarray);
   const { loading, error, apartments, hasMore } = getApartments(
      query,
      pageNum,
      selected
   );

   const observer = useRef<IntersectionObserver | null>(null);
   // prevents the infinite scroll from triggering forever
   const lastAptElementRef = useCallback(
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

   const handleToggle = (
      event: React.SyntheticEvent<Element, Event>,
      newSelected: string[]
   ) => {
      // prevents "high-low" and "low-high" from being selected at the same time
      const newPrice: string[] = [];
      const newPopular: string[] = [];
      if (newSelected.includes('low-high')) {
         newPrice.push('low-high');
      }
      if (newSelected.includes('high-low')) {
         newPrice.push('high-low');
      }
      if (newSelected.includes('least popular')) {
         newPrice.push('least popular');
      }
      if (newSelected.includes('most popular')) {
         newPrice.push('most popular');
      }
      newSelected = [...newPrice, ...newPopular];
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
         searchParams.set('popular', 'True');
      } else if (newSelected.includes('least popular')) {
         searchParams.set('ratingSort', '-1');
         searchParams.set('popular', 'True');
      } else {
         searchParams.delete('ratingSort');
         searchParams.delete('popular');
      }
      searchParams.set('populate', 'True');
      if (newSelected.length == 0) {
         searchParams.set('populate', 'False');
      }
      setSearchParams(searchParams);
   };

   return (
      <div className="App">
         <div>
            <br />
            <ToggleButtonGroup
               color="primary"
               value={selected}
               onChange={handleToggle}
               aria-label="Platform"
            >
               <ToggleButton value="low-high">Low-High</ToggleButton>
               <ToggleButton value="high-low">High-Low</ToggleButton>
               <ToggleButton value="least popular">Least Popular</ToggleButton>
               <ToggleButton value="most popular">Most Popular</ToggleButton>
            </ToggleButtonGroup>
            <br />
            <br />
            <br />
            <div>{apartments.length === 0 && !loading && 'None found'}</div>
            <div>
               {apartments.map((apartment, i) => {
                  if (apartments.length === i + 1) {
                     return (
                        // handles last element
                        <div key={i} ref={lastAptElementRef}>
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
