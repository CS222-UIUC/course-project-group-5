import { ToggleButton, ToggleButtonGroup } from '@mui/material';
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
   // eslint-disable-next-line
   const query = '';
   const [searchParams, setSearchParams] = useSearchParams();
   const [pageNum, setPageNum] = useState(1);
   // eslint-disable-next-line
   const [id, setId] = useState(-1);
   const [priceSort, setPriceSort] = useState('');
   const [ratingSort, setRatingSort] = useState('');
   const { loading, error, apartments, hasMore } = getApartments(
      query,
      pageNum,
      priceSort,
      ratingSort
   );
   const observer = useRef<IntersectionObserver | null>(null);
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

   const handlePriceToggle = (
      event: React.SyntheticEvent<Element, Event>,
      newSelected: string
   ) => {
      setPriceSort(newSelected);
      // sets URL
      if (newSelected === 'low-high') {
         searchParams.set('priceSort', '-1');
      } else if (newSelected === 'high-low') {
         searchParams.set('priceSort', '1');
      } else {
         searchParams.delete('priceSort');
      }
      searchParams.set('populate', 'True');
      if (newSelected) {
         searchParams.set('populate', 'False');
      }
      setSearchParams(searchParams);
   };

   const handlePopularToggle = (
      event: React.SyntheticEvent<Element, Event>,
      newSelected: string
   ) => {
      setRatingSort(newSelected);
      // sets URL
      if (newSelected === 'most popular') {
         searchParams.set('ratingSort', '1');
      } else if (newSelected === 'least popular') {
         searchParams.set('ratingSort', '-1');
      } else {
         searchParams.delete('ratingSort');
      }
      if (newSelected) {
         searchParams.set('populate', 'True');
         searchParams.set('numApts', '10');
      } else {
         searchParams.set('populate', 'False');
         searchParams.delete('numApts');
      }
      setSearchParams(searchParams);
   };

   return (
      <div className="App">
         <div>
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
            </div>
            <div>{loading && 'Loading...'}</div>
            <div>{error && 'Error...'}</div>
         </div>
      </div>
   );
}
