import React, { useEffect } from 'react';
import {
   Grid,
   Typography,
   List,
   ListItemText,
   Box,
   Divider,
   Stack,
   Button,
   ListItemAvatar,
   Avatar,
   ListItem,
   AppBar,
   Toolbar,
} from '@mui/material';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import PersonIcon from '@mui/icons-material/Person';
import getInfo from '../components/user/getUser';
import { logout } from '../components/user/LogOut';
import { FormEmail } from '../components/user/FormEmail';
import { FormPhone } from '../components/user/FormPhone';
import { FormLikedApts } from '../components/user/FormLikedApts';
import { useState, Dispatch, SetStateAction } from 'react';
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

interface UserProps {
   setId: Dispatch<SetStateAction<number>>;
}

function FormUser({ setId }: UserProps) {
   const user_info = getInfo();
   const [displayEmail, setDisplayEmail] = useState('');
   const [displayPhone, setDisplayPhone] = useState('');
   useEffect(() => {
      setDisplayEmail(user_info.user.email);
      setDisplayPhone(user_info.user.phone);
      setId(user_info.user.user_id);
   }, [user_info.user.email, user_info.user.phone, user_info.user.user_id]);
   return (
      <React.Fragment>
         {/* Form UI for user info */}
         <List>
            <ListItem>
               <ListItemAvatar>
                  <Avatar>
                     <PersonIcon />
                  </Avatar>
               </ListItemAvatar>
               <ListItemText
                  primary="Username"
                  secondary={user_info.user.username}
               />
            </ListItem>
            <Divider />
            <FormEmail
               displayEmail={displayEmail}
               setDisplayEmail={setDisplayEmail}
            />
            <Divider />
            <FormPhone
               displayPhone={displayPhone}
               setDisplayPhone={setDisplayPhone}
            />
         </List>
      </React.Fragment>
   );
}
