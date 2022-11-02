import React from 'react';
import Populate from '../components/populateLeft';
import SearchBar from '../components/SearchBar';

function MainPage() {
   //const [to, setTo] = useState(data[0]);
   return (
      <div>
         <SearchBar />
         <Populate />
      </div>
   );
}

export default MainPage;
