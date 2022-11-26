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
   return (
      <>
         <Grid container spacing={2}>
            <Grid item xs={3}>
               <FormUser/>
            </Grid>

            <Grid item xs={7}>
               <FormLikedApts/>
            </Grid>
         </Grid>
      </>
   );
}

function FormUser() {
   const user_info = getUser("");
   return (
      <React.Fragment>
         <List>
            <ListItemButton>
               <ListItemIcon>
                  <PersonIcon/>
               </ListItemIcon>
               <ListItemText primary={ user_info.user.username }/>
            </ListItemButton>

            <Divider />

            <ListItemButton>
               <ListItemText inset primary="Change password"/>
            </ListItemButton>

            <Divider />

            <ListItemButton>
               <ListItemIcon>
                  <EmailIcon/>
               </ListItemIcon>
               <ListItemText primary={ user_info.user.email } secondary=""/>
            </ListItemButton>

            <Divider />

            <ListItemButton>
               <ListItemIcon>
                  <PhoneIcon/>
               </ListItemIcon>
               <ListItemText primary={ user_info.user.phone }/>
            </ListItemButton>
         </List>
      </React.Fragment>
   );
}

function FormLikedApts() {
   const reviewed_apts = getReviewedApts("");
   return (
      <React.Fragment>
         <Box>
            <Stack spacing={2}>
               {reviewed_apts.apartments.map((apt, i) => {
                  return (
                     <Button variant="outlined">
                        {apt.name + " " + apt.address}
                        onClick = {}
                     </Button>
                  );
               })}
            </Stack>
         </Box>
      </React.Fragment>
   );
}
