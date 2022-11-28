import React from 'react';
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
   TextField,
   AppBar,
   Toolbar,
} from '@mui/material';
import EmailIcon from '@mui/icons-material/Email';
import PhoneIcon from '@mui/icons-material/Phone';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import PersonIcon from '@mui/icons-material/Person';
import getReviewedApts from '../components/user/getReviewedApts';
import getUser from '../components/user/getUser';
import {
   changeEmail,
   changePhone,
   logout,
} from '../components/user/changeInfo';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function User() {
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
                  <FormUser />
                  <Button variant="outlined" style={btnstyle}>
                     <Typography variant="subtitle2">
                        Change Password
                     </Typography>
                  </Button>
               </Grid>

               <Grid item xs={7}>
                  <FormLikedApts />
               </Grid>
            </Grid>
         </Stack>
      </>
   );
}

function FormUser() {
   const user_info = getUser('Zongxian');
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
            <FormEmail email={user_info.user.email} />
            <Divider />
            <FormPhone phone={user_info.user.phone} />
         </List>
      </React.Fragment>
   );
}

interface EmailComponentProps {
   email: string;
}

function FormEmail({ email }: EmailComponentProps) {
   const [editEmail, setChangeEmail] = useState(false);
   const [newEmail, setNewEmail] = useState('');
   return (
      <React.Fragment>
         {/* Email box changes based on click */}
         {editEmail === false && (
            <ListItem>
               <ListItemAvatar>
                  <Avatar>
                     <EmailIcon />
                  </Avatar>
               </ListItemAvatar>
               <ListItemText primary="Email" secondary={email} />
               <Button
                  color="primary"
                  variant="outlined"
                  onClick={() => setChangeEmail(true)}
               >
                  <Typography variant="subtitle2">Change email</Typography>
               </Button>
            </ListItem>
         )}
         {editEmail === true && (
            <ListItem>
               <Grid container spacing={1}>
                  <Grid item xs={12}>
                     <TextField
                        label="Email"
                        variant="outlined"
                        fullWidth
                        onChange={(event) => {
                           setNewEmail(event.target.value);
                        }}
                     />
                  </Grid>
                  <Grid item xs>
                     <Box display="flex" justifyContent="flex-end">
                        <Button
                           type="submit"
                           color="primary"
                           variant="contained"
                           size="small"
                           onClick={() => setChangeEmail(false)}
                        >
                           Cancel
                        </Button>
                     </Box>
                  </Grid>
                  <Grid item xs={2}>
                     <Box display="flex" justifyContent="flex-end">
                        <Button
                           type="submit"
                           color="primary"
                           variant="contained"
                           size="small"
                           onClick={() => changeEmail(newEmail)}
                        >
                           Submit
                        </Button>
                     </Box>
                  </Grid>
               </Grid>
            </ListItem>
         )}
      </React.Fragment>
   );
}

interface PhoneComponentProps {
   phone: string;
}

function FormPhone({ phone }: PhoneComponentProps) {
   const [editPhone, setChangePhone] = useState(false);
   const [newPhone, setNewPhone] = useState('');
   return (
      <React.Fragment>
         {/* Phone box changes based on click */}
         {editPhone === false && (
            <ListItem>
               <ListItemAvatar>
                  <Avatar>
                     <PhoneIcon />
                  </Avatar>
               </ListItemAvatar>
               <ListItemText primary="Phone number" secondary={phone} />
               <Button
                  color="primary"
                  variant="outlined"
                  onClick={() => {
                     setChangePhone(true);
                  }}
               >
                  <Typography variant="subtitle2">Change phone</Typography>
               </Button>
            </ListItem>
         )}
         {editPhone === true && (
            <ListItem>
               <Grid container spacing={1}>
                  <Grid item xs={12}>
                     <TextField
                        label="Phone"
                        variant="outlined"
                        fullWidth
                        onChange={(event) => {
                           setNewPhone(event.target.value);
                        }}
                     />
                  </Grid>
                  <Grid item xs>
                     <Box display="flex" justifyContent="flex-end">
                        <Button
                           type="submit"
                           color="primary"
                           variant="contained"
                           size="small"
                           onClick={() => setChangePhone(false)}
                        >
                           Cancel
                        </Button>
                     </Box>
                  </Grid>
                  <Grid item xs={2}>
                     <Box display="flex" justifyContent="flex-end">
                        <Button
                           type="submit"
                           color="primary"
                           variant="contained"
                           size="small"
                           onClick={() => changePhone(newPhone)}
                        >
                           Submit
                        </Button>
                     </Box>
                  </Grid>
               </Grid>
            </ListItem>
         )}
      </React.Fragment>
   );
}

function FormLikedApts() {
   console.log('Getting apt info');
   const reviewed_apts = getReviewedApts('Zongxian');
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
