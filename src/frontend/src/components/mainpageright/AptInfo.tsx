import * as React from 'react';
import { AptType } from '../Types';
import { Stack, Box, Typography, Paper } from '@mui/material';

export interface IAptInfoProps {
   apt: AptType | undefined;
}

export function AptInfo({ apt }: IAptInfoProps) {
   return (
      <React.Fragment>
         <Paper elevation={3}>
            <Stack>
               <Box display="flex" justifyContent="center">
                  <Typography variant="h4">{apt?.name}</Typography>
               </Box>
               <Box display="flex" justifyContent="center">
                  <Typography variant="h6">{apt?.address}</Typography>
               </Box>
               <Box display="flex" justifyContent="center">
                  <Typography variant="h6">
                     Price Range: ${apt?.price_min}~${apt?.price_max}
                  </Typography>
               </Box>
               <Box display="flex" justifyContent="center">
                  <Typography variant="h6">
                     Rating: ${apt?.votes || 0}
                  </Typography>
               </Box>
            </Stack>
         </Paper>
      </React.Fragment>
   );
}
