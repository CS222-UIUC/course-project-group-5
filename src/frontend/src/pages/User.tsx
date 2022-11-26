import React from 'react';
import {
   Grid,
   TextField,
   Typography,
   List,
   ListItemButton,
   ListItemText,
   ListItemIcon,
   Box,
   Divider,
   Stack,
   Button,
   Link,
   ListItemAvatar,
   Avatar,
   ListItem,
   AvatarGroup
} from '@mui/material';
import EmailIcon from '@mui/icons-material/Email';
import PhoneIcon from '@mui/icons-material/Phone';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import PersonIcon from '@mui/icons-material/Person';
import axios from 'axios';
import { useState } from 'react';
import getReviewedApts from '../components/user/getReviewedApts';
import getUser from '../components/user/getUser';


export default function User() {
   const btnstyle = { marginLeft: '10px' };
   return (
      <>
         <Grid container spacing={2}>
            <Grid item xs={4}>
               <FormUser/>
               <Button variant="outlined" style={btnstyle}>
                  <Typography variant="subtitle2">
                     Change Password
                  </Typography>
               </Button>
            </Grid>

            <Grid item xs={7}>
               <FormLikedApts/>
            </Grid>
         </Grid>
      </>
   );
}

function FormUser() {
   const user_info = getUser("Zongxian");
   return (
      <React.Fragment>
         <List>
            <ListItem>
               <ListItemAvatar>
                  <Avatar>
                     <PersonIcon/>
                  </Avatar>
               </ListItemAvatar>
               <ListItemText primary="Username" secondary={ user_info.user.username }/>
            </ListItem>

            <Divider />

            <ListItem>
               <ListItemAvatar>
                  <Avatar>
                     <EmailIcon/>
                  </Avatar>
               </ListItemAvatar>
               <ListItemText primary="Email" secondary={ user_info.user.email }/>
               <Button color="primary" variant="outlined">
                  <Typography variant="subtitle2">
                     Change email
                  </Typography>
               </Button>
            </ListItem>

            <Divider />

            <ListItem>
               <ListItemAvatar>
                  <Avatar>
                     <EmailIcon/>
                  </Avatar>
               </ListItemAvatar>
               <ListItemText primary="Phone number" secondary={ user_info.user.phone }/>
               <Button color="primary" variant="outlined">
                  <Typography variant="subtitle2">
                     Change phone
                  </Typography>
               </Button>
            </ListItem>
         </List>
      </React.Fragment>
   );
}

function FormLikedApts() {
   console.log("Getting apt info")
   const reviewed_apts = getReviewedApts("Zongxian");
   return (
      <React.Fragment>
         <Box>
            <Stack spacing={2}>
               {reviewed_apts.apartments.map((apt, i) => {
                  return (
                     <Button variant="outlined" key={i} onClick={() => {
                        console.log("Getting apt info")
                     }}>
                        {apt.name + " " + apt.address}
                     </Button>
                  );
               })}
            </Stack>
         </Box>
      </React.Fragment>
   );
}
