import { Autocomplete, Stack, TextField } from '@mui/material';
import React, { useState } from 'react';
import data from '../staticdata.json';
import { useSearchParams } from 'react-router-dom';
import './SearchBarStyles.css';
import getSuggestions from './getSearchBarSuggestions';

export default function SearchBar() {
   // eslint-disable-next-line
   const [query, setQuery] = useState('');
   const [searchParams, setSearchParams] = useSearchParams();
   const [search, setSearch] = useState(false);
   // eslint-disable-next-line
   const { names } = getSuggestions(query, search);

   const handleSubmit = (
      event: React.SyntheticEvent<Element, Event>,
      value: string
   ) => {
      event.preventDefault();
      setQuery(value);
      if (value === '') {
         searchParams.delete('searchQuery');
         searchParams.set('search', 'False');
         setSearch(false);
      } else {
         searchParams.set('searchQuery', value);
         searchParams.set('search', 'True');
         setSearch(true);
      }
      setSearchParams(searchParams);
   };

   return (
      <>
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
      </>
   );
}
