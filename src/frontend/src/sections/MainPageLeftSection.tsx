import React from 'react';
import Searching from '../components/Searching';

interface props {
   selectApt: any;
   onSelect: any;
}

export default function LeftSection() {
   return (
      <div style={{ marginTop: '200px' }}>
         <Searching />
      </div>
   );
}
