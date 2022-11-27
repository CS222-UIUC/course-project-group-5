import React, { useState } from 'react';
import getApartments from '../components/mainpageleft/getApts';
import Populate from '../components/mainpageleft/PopulateLeftSection';
import SearchBar from '../components/SearchBar';
import { AptType } from '../components/Types';
import RightSection from '../sections/MainPageRightSection';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import { logout } from '../components/user/changeInfo';
import { useNavigate } from 'react-router-dom';

import {
   Stack,
   AppBar,
   Toolbar,
   Grid,
   Box,
   Avatar,
   Button,
} from '@mui/material';

function MainPage() {
   const navigate = useNavigate();
   const { apartments } = getApartments('0', '0', -1);
   const [to, setTo] = useState<AptType>(apartments[0]);
   return (
      <>
         <Stack spacing={2}>
            {/* Top bar */}
            <AppBar component="nav">
               <Toolbar>
                  <Grid container spacing={0}>
                     <Grid item>
                        <Box>
                           <Avatar>
                              <AccountCircleIcon />
                           </Avatar>
                        </Box>
                     </Grid>
                     <Grid item>
                        <Box>
                           <Button
                              sx={{ color: '#fff' }}
                              onClick={() => navigate('/user')}
                           >
                              User
                           </Button>
                        </Box>
                     </Grid>
                     <Grid item xs={10}>
                        <Box>
                           <Button sx={{ color: '#fff' }}>About</Button>
                        </Box>
                     </Grid>
                     <Grid item>
                        <Box
                           display="flex"
                           justifyContent="flex-end"
                           alignItems="flex-end"
                        >
                           <Button
                              sx={{ color: '#fff' }}
                              onClick={() => {
                                 logout();
                                 navigate('/login');
                              }}
                           >
                              Log out
                           </Button>
                        </Box>
                     </Grid>
                  </Grid>
               </Toolbar>
            </AppBar>
            <Grid container spacing={3}>
               {/* Search bar and rest of the components */}
               <Grid item xs={12}>
                  <Box
                     display="flex"
                     justifyContent="center"
                     alignItems="center"
                  >
                     <Stack spacing={2} sx={{ width: 300 }}>
                        <SearchBar />
                     </Stack>
                  </Box>
               </Grid>
               <Grid item xs={3}>
                  <Populate onSelect={(apt) => setTo(apt)} />
               </Grid>
               <Grid item xs>
                  <RightSection apt={to || apartments[0]} />
               </Grid>
            </Grid>
         </Stack>
      </>
   );
}
export default MainPage;
