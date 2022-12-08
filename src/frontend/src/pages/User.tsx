import React from 'react';
import {
   Grid,
   Typography,
   Box,
   Stack,
   Button,
   Avatar,
   AppBar,
   Toolbar,
} from '@mui/material';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import { logout } from '../components/user/LogOut';
import { FormUser } from '../components/user/FormUser';
import { FormLikedApts } from '../components/user/FormLikedApts';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function User() {
   const [id, setId] = useState(-1);
   const navigate = useNavigate();
   const btnstyle = { marginLeft: '10px' };
   return (
      <>
         <Stack spacing={1}>
            <AppBar component="nav">
               {/*Renders top bar*/}
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
                              onClick={() => navigate('/')}
                           >
                              Main
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
            <Grid container spacing={2}>
               {/*Headers*/}
               <Grid item xs={4}>
                  <Box display="flex" justifyContent="center">
                     <Typography variant="h4">User</Typography>
                  </Box>
               </Grid>
               <Grid item xs={7}>
                  <Box display="flex" justifyContent="center">
                     <Typography variant="h4">Reviewed Apartments</Typography>
                  </Box>
               </Grid>
            </Grid>
            <Grid container spacing={2}>
               {/* User info and list of reviewed apts */}
               <Grid item xs={4}>
                  <FormUser setId={setId} />
                  <Button variant="outlined" style={btnstyle}>
                     <Typography variant="subtitle2">
                        Change Password
                     </Typography>
                  </Button>
               </Grid>

               <Grid item xs={7}>
                  <FormLikedApts id={id} />
               </Grid>
            </Grid>
         </Stack>
      </>
   );
}
