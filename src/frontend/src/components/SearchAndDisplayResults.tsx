import { ToggleButton, ToggleButtonGroup } from '@mui/material';
import React, { useState, useRef, useCallback, KeyboardEvent } from 'react';
import SingleCard from './SingleCard';
import useSearchApartment from './getsApartments';
import SearchBar from './SearchBar';

export default function Searching() {
   const [query, setQuery] = useState('');
   const [pageNum, setPageNum] = useState(1);
   const [press, setPress] = useState(false);
   const emptyarray: string[] = [];
   const [selected, setSelected] = useState(emptyarray);
   const { loading, error, apartments, hasMore } = useSearchApartment(
      query,
      pageNum,
      press,
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

   /*const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
      setQuery(e.target.value);
      setPageNum(1);
      setPress(false);
   };

   const handlePress = (e: KeyboardEvent<HTMLInputElement>) => {
      // POST request when enter is pressed
      if (e.key === 'Enter') {
         e.preventDefault();
         setPress(true);
      }
   };

   function handlePost(query: string, select: string[]) {
      // POST request of the query and buttons selected
      axios({
         method: 'POST',
         url: 'http://localhost:3333/mockdata',
         data: {
            q: query,
            selected: select,
         },
         headers: {
            'Content-Type': 'application/json',
         },
      })
         .then((response) => {
            console.log(response);
         })
         .catch((error) => {
            if (error.response) {
               console.log(error.response);
               console.log(error.response.status);
               console.log(error.response.headers);
            }
         });
   }*/

   //useEffect(() => {
   // triggers a post request whenever a button is selected
   //   handlePost(query, selected);
   //}, [selected]);

   const handleToggle = (
      event: React.MouseEvent<HTMLElement>,
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
   };

   return (
      <div className="App">
         <div>
            <div style={{ display: 'flex', justifyContent: 'center' }}>
               {/*<div className="search" style={{ width: '800px' }}>
                  <TextField
                     id="outlined-basic"
                     variant="outlined"
                     fullWidth
                     value={query || ''}
                     label="Apartment Search"
                     onKeyDown={handlePress}
                     onChange={handleChange}
                  />
               </div>*/}
            </div>
            <SearchBar />
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
               {press && apartments.length === 0 && !loading && 'None found'}
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
            <div>{press && loading && 'Loading...'}</div>
            <div>{press && error && 'Error...'}</div>
         </div>
      </div>
   );
}