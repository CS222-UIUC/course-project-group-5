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
} from '@mui/material';
import EmailIcon from '@mui/icons-material/Email';
import PhoneIcon from '@mui/icons-material/Phone';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import PersonIcon from '@mui/icons-material/Person';
import getReviewedApts from '../components/user/getReviewedApts';
import getUser from '../components/user/getUser';
import {changeEmail, changePhone} from '../components/user/changeInfo';
import { useState } from 'react';


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
   const [editEmail, setChangeEmail] = useState(false);
   const [editPhone, setChangePhone] = useState(false);
   const [newEmail, setNewEmail] = useState("");
   const [newPhone, setNewPhone] = useState("");
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

            {editEmail == false && (
            <ListItem>
               <ListItemAvatar>
                  <Avatar>
                     <EmailIcon/>
                  </Avatar>
               </ListItemAvatar>
               <ListItemText primary="Email" secondary={ user_info.user.email }/>
               <Button color="primary" variant="outlined" onClick={() => 
                  setChangeEmail(true)
               }>
                  <Typography variant="subtitle2">
                     Change email
                  </Typography>
               </Button>
            </ListItem>)}

            {editEmail == true && (
            <ListItem>
               <Grid container spacing={1}>
                  <Grid item xs={12}>
                  <TextField label="Email" variant="outlined" fullWidth onChange={(event) => {
                        setNewEmail(event.target.value)
                     }}/>
                  </Grid>
                  <Grid item xs={4}>
                     <Button type="submit" color="primary" variant="contained" size="small" onClick={() => 
                        setChangeEmail(false)
                     }>
                        Cancel
                     </Button>
                  </Grid>
                  <Grid item xs={7}>
                     <Button type="submit" color="primary" variant="contained" size="small" onClick={() => 
                        changeEmail(newEmail, "Zongxian")
                     }>
                        Submit
                     </Button>
                  </Grid>
               </Grid>
            </ListItem>
            )}

            <Divider />

            {editPhone == false && (
            <ListItem>
               <ListItemAvatar>
                  <Avatar>
                     <PhoneIcon/>
                  </Avatar>
               </ListItemAvatar>
               <ListItemText primary="Phone number" secondary={ user_info.user.phone }/>
               <Button color="primary" variant="outlined" onClick={() => {
                  setChangePhone(true)
               }}>
                  <Typography variant="subtitle2">
                     Change phone
                  </Typography>
               </Button>
            </ListItem>)}

            {editPhone == true && (
            <ListItem>
               <Grid container spacing={1}>
                  <Grid item xs={12}>
                  <TextField label="Phone" variant="outlined" fullWidth onChange={(event) => {
                        setNewPhone(event.target.value)
                     }}/>
                  </Grid>
                  <Grid item xs={4}>
                     <Button type="submit" color="primary" variant="contained" size="small" onClick={() => 
                        setChangePhone(false)
                     }>
                        Cancel
                     </Button>
                  </Grid>
                  <Grid item xs={7}>
                     <Button type="submit" color="primary" variant="contained" size="small" onClick={() => 
                        changePhone(newPhone, "Zongxian")
                     }>
                        Submit
                     </Button>
                  </Grid>
               </Grid>
            </ListItem>
            )}

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
