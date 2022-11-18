import { Autocomplete, Stack, TextField } from '@mui/material';
import React, { useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.css';
import getSuggestions from './mainpageleft/getSearchBarSuggestions';

export default function SearchBar() {
   const [query, setQuery] = useState('');
   const [searchParams, setSearchParams] = useSearchParams();
   const [search, setSearch] = useState(false);
   const { names } = getSuggestions(query, search);

   const handleChange = (
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
      <nav className="navbar fixed-top navbar-light bg-light">
         <a className="navbar-brand">Apartment Search</a>
         <div className="text-center">
            <Stack spacing={2} sx={{ width: 500 }}>
               <Autocomplete
                  id="free-solo-demo"
                  freeSolo
                  onInputChange={handleChange}
                  options={names.map((option) => option.name)}
                  renderInput={(params) => (
                     <TextField {...params} label="Search" />
                  )}
               />
            </Stack>
         </div>
         <p>Hello, Zongxian</p>
      </nav>
   );
}
