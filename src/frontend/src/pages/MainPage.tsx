import React, { useEffect, useState } from 'react';
import getApartments from '../components/mainpageleft/getApts';
import Populate from '../components/mainpageleft/PopulateLeftSection';
import SearchBar from '../components/SearchBar';
import { AptType } from '../components/Types';
import RightSection from '../sections/MainPageRightSection';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import { logout } from '../components/user/LogOut';
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
import axios from 'axios';

function MainPage() {
   const navigate = useNavigate();
   const { apartments } = getApartments('0', '0', -1);
   const [to, setTo] = useState<AptType>(apartments[0]);
   const [logged, setLogged] = useState(false);
   const [username, setUsername] = useState('');
   const handleAptChange = (apt: AptType) => {
      setTo(apt);
   };
   function checkLoggedIn() {
      axios({
         url: 'http://127.0.0.1:5000/api/whoami',
         withCredentials: true,
      })
         .then((response) => {
            console.log(response);
            setLogged(true);
            setUsername(response.data);
         })
         .catch((error) => {
            if (error.response) {
               console.log(error.response);
               console.log(error.response.status);
               console.log(error.response.headers);
            }
         });
   }
   useEffect(() => {
      checkLoggedIn();
   }, []);

   return (
      <>
         <Stack>
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
                     {logged === true && (
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
                     )}
                     <Grid item xs={logged === true ? 10 : 11}>
                        <Box>
                           <Button sx={{ color: '#fff' }}>About</Button>
                        </Box>
                     </Grid>
                     {logged === true && (
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
                     )}
                     {logged === false && (
                        <Grid item>
                           <Box
                              display="flex"
                              justifyContent="flex-end"
                              alignItems="flex-end"
                           >
                              <Button
                                 sx={{ color: '#fff' }}
                                 onClick={() => {
                                    navigate('/login');
                                 }}
                              >
                                 Log in
                              </Button>
                           </Box>
                        </Grid>
                     )}
                  </Grid>
               </Toolbar>
            </AppBar>
            <Grid container spacing={3}>
               {/* Search bar*/}
               <Grid item xs={12}>
                  <Box
                     display="flex"
                     justifyContent="center"
                     alignItems="center"
                  >
                     <Stack spacing={2} sx={{ width: 500 }}>
                        <SearchBar handleAptChange={handleAptChange} />
                     </Stack>
                  </Box>
               </Grid>
               {/* The rest of the components */}
               <Grid item xs={3}>
                  <Populate onSelect={(apt) => setTo(apt)} />
               </Grid>
               <Grid item xs style={{ maxHeight: '100%', overflow: 'auto' }}>
                  <RightSection
                     apt={to || apartments[0]}
                     logged={logged}
                     username={username}
                     handleAptChange={handleAptChange}
                  />
               </Grid>
            </Grid>
         </Stack>
      </>
   );
}
export default MainPage;
