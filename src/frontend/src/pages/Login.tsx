import React, { useEffect } from 'react';
import {
   Grid,
   Paper,
   TextField,
   Button,
   Typography,
   Link,
   FormControlLabel,
   Checkbox,
   Stack,
} from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import axios from 'axios';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function Login() {
   const navigate = useNavigate();
   const [user, setUser] = useState('');
   const [password, setPassword] = useState('');
   const [res, setRes] = useState();

   function sendData() {
      axios({
         method: 'post',
         url: 'http://127.0.0.1:5000/login',
         withCredentials: true,
         data: {
            user: user,
            password: password,
         },
      })
         .then((response) => {
            console.log(response);
            setRes(response.data);
         })
         .catch((error) => {
            if (error.response) {
               console.log(error.response);
               console.log(error.response.status);
               console.log(error.response.headers);
               setRes(error.response.data);
            }
         });
   }

   const paperStyle = {
      padding: 20,
      height: '100%',
      width: 310,
      margin: '20px auto',
   };
   useEffect(() => {
      if (res === `welcome ${user}`) {
         navigate('/');
      }
   }, [res, user]);

   const btnstyle = { margin: '8px 0' };
   return (
      <Grid>
         <Paper elevation={12} style={paperStyle}>
            <Stack spacing={2}>
               {/* A paper like UI with fields for login */}
               <Grid container spacing={2}>
                  <Grid item xs={2}>
                     <PersonIcon fontSize="large" />
                  </Grid>
                  <Grid item xs>
                     <h2>Sign In</h2>
                  </Grid>
               </Grid>
               <TextField
                  label="Username/Email"
                  placeholder="Enter Username or Email"
                  onChange={(event) => setUser(event.target.value)}
                  fullWidth
                  required
               />
               <TextField
                  label="Password"
                  placeholder="Enter Password"
                  type="password"
                  onChange={(event) => setPassword(event.target.value)}
                  fullWidth
                  required
               />
               <FormControlLabel
                  control={<Checkbox name="checkedB" color="primary" />}
                  label="Remember me"
               />
               <Button
                  type="submit"
                  color="primary"
                  variant="contained"
                  style={btnstyle}
                  onClick={sendData}
                  fullWidth
               >
                  Sign in
               </Button>
            </Stack>
            <Typography>
               <Link href="#">Forgot Password</Link>
            </Typography>
            <Typography>
               <Link href="/register">Sign Up</Link>
            </Typography>
            <Typography>
               <Link href="/">Access without logging in</Link>
            </Typography>
            {res !== undefined && res !== `welcome ${user}` && (
               <Typography sx={{ color: '#ff0000' }}>{res}</Typography>
            )}
         </Paper>
      </Grid>
   );
}
