import React from 'react';
import { Box, Stack, Button } from '@mui/material';
import getReviewedApts from './getReviewedApts';

interface LikedAptsProps {
   id: number;
}

export function FormLikedApts({ id }: LikedAptsProps) {
   console.log('Getting apt info');
   const reviewed_apts = getReviewedApts(id);
   return (
      <React.Fragment>
         {/* UI for liked apartments */}
         <Box>
            <Stack spacing={2}>
               {reviewed_apts.apartments.map((apt, i) => {
                  return (
                     <Button
                        variant="outlined"
                        key={i}
                        onClick={() => {
                           console.log('Getting apt info');
                        }}
                     >
                        {apt.name + ' ' + apt.address}
                     </Button>
                  );
               })}
            </Stack>
         </Box>
      </React.Fragment>
   );
}
