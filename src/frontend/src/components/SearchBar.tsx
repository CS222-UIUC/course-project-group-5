import { Autocomplete, TextField } from '@mui/material';
import React, { useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import './SearchBarStyles.css';
import getSuggestions from './mainpageleft/getSearchBarSuggestions';
import { AptType } from './Types';
import axios from 'axios';
interface Props {
   handleAptChange: (apt: AptType) => void;
}

const baseURL = 'http://127.0.0.1:5000/main';
export default function SearchBar({ handleAptChange }: Props) {
   const [query, setQuery] = useState('');
   const [searchParams, setSearchParams] = useSearchParams();
   const [search, setSearch] = useState(false);
   const { apts } = getSuggestions(query, search);
   const queryApt = (id: number) => {
      axios({
         method: 'GET',
         url: `${baseURL}?search=True&aptId=${id}`,
      })
         .then((response) => {
            console.log(response);
            handleAptChange({
               id: response.data.apt_id,
               name: response.data.name,
               address: response.data.address,
               price_min: response.data.price_min,
               price_max: response.data.price_max,
               rating: response.data.rating,
            });
         })
         .catch((error) => {
            if (error.response) {
               console.log(error.response);
               console.log(error.response.status);
               console.log(error.response.headers);
            }
         });
   };
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
      <React.Fragment>
         {/* Search bar with autocomplete from the server */}
         <Autocomplete
            id="free-solo-demo"
            freeSolo
            onInputChange={handleChange}
            onChange={(event, value) => {
               console.log(event);
               queryApt((value as AptType).id);
            }}
            options={apts}
            getOptionLabel={(option) => (option as AptType).name}
            //.map((option) => option.name)
            filterOptions={(x) => x}
            renderInput={(params) => (
               <TextField {...params} label="Search apartments" />
            )}
         />
      </React.Fragment>
   );
}
