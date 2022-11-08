import { Grid, ToggleButton, ToggleButtonGroup } from '@mui/material';
import React, { useState, useRef, useCallback } from 'react';
import SingleCard from './SingleCard';
import { useSearchParams } from 'react-router-dom';
import './SearchBarStyles.css';
import getApartments from './getApts';
import { AptType } from './Types';

interface Props {
   onSelect: (apt: AptType) => void;
}

export default function Populate({ onSelect }: Props) {
   const [searchParams, setSearchParams] = useSearchParams();
   const [id, setId] = useState(-1);
   const [priceSort, setPriceSort] = useState('');
   const [ratingSort, setRatingSort] = useState('');
   const { loading, error, apartments, hasMore } = getApartments(
      priceSort,
      ratingSort,
      id
   );
   const observer = useRef<IntersectionObserver | null>(null);
   /* 
   called when the user reaching the last div element (bottom of screen)
   sets url for populate and Id
   gets the last div element's Id
   */
   const lastAptElementRef = useCallback(
      (node: HTMLDivElement) => {
         if (loading) return;
         if (observer.current) observer.current.disconnect();
         observer.current = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting && hasMore) {
               const lastId = apartments.at(-1)?.id || -1;
               setId(lastId); // last element's id or -1 if null
               searchParams.set('aptId', '' + lastId);
               searchParams.set('populate', 'True');
               setSearchParams(searchParams);
            }
         });
         if (node) observer.current.observe(node);
      },
      [loading, hasMore]
   );

   const handlePriceToggle = (
      event: React.SyntheticEvent<Element, Event>,
      selected: string
   ) => {
      setPriceSort(selected);
      setId(-1); // start at the beginning
      // sets URL
      if (selected === 'low-high') {
         searchParams.set('priceSort', '-1');
      } else if (selected === 'high-low') {
         searchParams.set('priceSort', '1');
      } else {
         searchParams.delete('priceSort');
      }
      searchParams.set('populate', 'True');
      if (selected) {
         searchParams.set('populate', 'False');
      }
      setSearchParams(searchParams);
   };

   const handlePopularToggle = (
      event: React.SyntheticEvent<Element, Event>,
      selected: string
   ) => {
      setRatingSort(selected);
      setId(-1); // start at the beginning
      // sets URL
      searchParams.delete('aptId');
      if (selected === 'most popular') {
         searchParams.set('ratingSort', '1');
      } else if (selected === 'least popular') {
         searchParams.set('ratingSort', '-1');
      } else {
         searchParams.delete('ratingSort');
      }
      if (selected) {
         searchParams.set('populate', 'True');
         searchParams.set('numApts', '10');
      } else {
         searchParams.delete('numApts');
      }
      setSearchParams(searchParams);
   };

   return (
      <>
         <div>
            <div style={{ textAlign: 'center' }}>
               <br />
               <ToggleButtonGroup
                  color="primary"
                  value={priceSort}
                  onChange={handlePriceToggle}
                  aria-label="Platform"
                  exclusive
               >
                  <ToggleButton value="low-high">Low-High</ToggleButton>
                  <ToggleButton value="high-low">High-Low</ToggleButton>
               </ToggleButtonGroup>
               <ToggleButtonGroup
                  color="primary"
                  value={ratingSort}
                  onChange={handlePopularToggle}
                  aria-label="Platform"
                  exclusive
               >
                  <ToggleButton value="least popular">
                     Least Popular
                  </ToggleButton>
                  <ToggleButton value="most popular">Most Popular</ToggleButton>
               </ToggleButtonGroup>
            </div>
            <br />
            <br />
            <br />
            <div style={{ textAlign: 'center' }}>
               {apartments.length === 0 && !loading && 'None found'}
            </div>
            <Grid style={{ maxHeight: '100vh', overflow: 'auto' }}>
               {apartments.map((apartment, i) => {
                  if (apartments.length === i + 1) {
                     return (
                        // handles last element
                        <div key={i} ref={lastAptElementRef}>
                           <SingleCard
                              {...apartment}
                              key={i}
                              onSelect={onSelect}
                           />
                        </div>
                     );
                  } else {
                     return (
                        <div key={i}>
                           <SingleCard
                              {...apartment}
                              key={i}
                              onSelect={onSelect}
                           />
                        </div>
                     );
                  }
               })}
            </Grid>
            <div style={{ textAlign: 'center' }}>{loading && 'Loading...'}</div>
            <div style={{ textAlign: 'center' }}>{error && 'Error...'}</div>
         </div>
      </>
   );
}
