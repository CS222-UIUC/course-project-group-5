import React from 'react';
// import { AptType } from '../components/Types';
import LeftSection from '../sections/MainPageLeftSection';
import RightSection from '../sections/MainPageRightSection';

function MainPage() {
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
               <LeftSection />
            </div>
            <div className="w-50">
               <RightSection apt={apt} />
            </div>
         </div>
      </div>
   );
}
export default MainPage;
