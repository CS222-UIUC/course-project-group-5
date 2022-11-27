import {
   Grid,
   Paper,
   FormControl,
   Select,
   MenuItem,
   SelectChangeEvent,
   InputLabel,
   Stack,
   Typography,
   Box,
} from '@mui/material';
import React, { useState, useRef, useCallback } from 'react';
import SingleCard from '../SingleCard';
import { useSearchParams } from 'react-router-dom';
import '../SearchBarStyles.css';
import getApartments from './getApts';
import { AptType } from '../Types';

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

   const handlePriceToggle = (event: SelectChangeEvent<string>) => {
      setPriceSort(event.target.value);
      setId(-1); // start at the beginning
      // sets URL
      if (event.target.value === 'low-high') {
         searchParams.set('priceSort', '-1');
      } else if (event.target.value === 'high-low') {
         searchParams.set('priceSort', '1');
      } else {
         searchParams.delete('priceSort');
      }
      searchParams.set('populate', 'True');
      if (event.target.value) {
         searchParams.set('populate', 'False');
      }
      setSearchParams(searchParams);
   };

   const handlePopularToggle = (event: SelectChangeEvent<string>) => {
      setRatingSort(event.target.value);
      setId(-1); // start at the beginning
      // sets URL
      searchParams.delete('aptId');
      if (event.target.value === 'most popular') {
         searchParams.set('ratingSort', '1');
      } else if (event.target.value === 'least popular') {
         searchParams.set('ratingSort', '-1');
      } else {
         searchParams.delete('ratingSort');
      }
      if (event.target.value) {
         searchParams.set('populate', 'True');
         searchParams.set('numApts', '10');
      } else {
         searchParams.delete('numApts');
      }
      setSearchParams(searchParams);
   };

   return (
      <React.Fragment>
         <Stack spacing={3}>
            <Paper elevation={2}>
               <Grid container justifyContent="space-between">
                  <Grid item xs={5}>
                     <FormControl fullWidth>
                        <InputLabel>Price</InputLabel>
                        <Select
                           size="medium"
                           color="primary"
                           onChange={handlePriceToggle}
                           label="Price"
                        >
                           <MenuItem value="low-high">Low to High</MenuItem>
                           <MenuItem value="high-low">High to Low</MenuItem>
                        </Select>
                     </FormControl>
                  </Grid>
                  <Grid item xs={5}>
                     <FormControl fullWidth>
                        <InputLabel>Popularity</InputLabel>
                        <Select
                           size="medium"
                           color="primary"
                           onChange={handlePopularToggle}
                           label="Popularity"
                        >
                           <MenuItem value="least popular">
                              Least Popular
                           </MenuItem>
                           <MenuItem value="most popular">
                              Most Popular
                           </MenuItem>
                        </Select>
                     </FormControl>
                  </Grid>
               </Grid>
            </Paper>
            {apartments.length === 0 && !loading && (
               <Box display="flex" justifyContent="center">
                  <Typography variant="h5">None found</Typography>
               </Box>
            )}
            <Stack style={{ maxHeight: '175vh', overflow: 'auto' }} spacing={2}>
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
            </Stack>
            {loading && (
               <Box display="flex" justifyContent="center">
                  <Typography variant="h5">Loading...</Typography>
               </Box>
            )}
            {error && (
               <Box display="flex" justifyContent="center">
                  <Typography variant="h5">Error...</Typography>
               </Box>
            )}
         </Stack>
      </React.Fragment>
   );
}
