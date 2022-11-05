import React from 'react';
import Populate from '../components/PopulateLeft';
import SearchBar from '../components/SearchBar';
// import { AptType } from '../components/Types';
import RightSection from '../sections/MainPageRightSection';

function MainPage() {
   //const [to, setTo] = useState(data[0]);
   // uncommented when left and right connected
   // const [apt, setApt] = useState<AptType>({
   //    id: 2,
   //    name: 'sample apartment',
   //    address: 'sample address',
   //    price_min: 0,
   //    price_max: 0,
   //    votes: 0,
   // });
   const apt = {
      id: 2,
      name: 'sample apartment',
      address: 'sample address',
      price_min: 0,
      price_max: 0,
      votes: 0,
   };

   return (
      <div>
         <div className="d-flex flex-row">
            <div className="w-50">
               <SearchBar />
               <Populate />
            </div>
            <div className="w-50">
               <RightSection apt={apt} />
            </div>
         </div>
      </div>
   );
}
export default MainPage;
