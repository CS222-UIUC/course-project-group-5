import React from 'react';
import {
   Grid,
   Paper,
   TextField,
   Button,
   Typography,
   Link,
   FormControlLabel,
   Checkbox,
} from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';
import axios from 'axios';
import { useState } from 'react';

function sendData(username: string, email: string, password: string) {
   axios({
      method: 'post',
      url: '/login',
      data: {
         username: username,
         email: email,
         password: password,
      },
   })
      .then((response) => {
         console.log(response);
      })
      .catch((error) => {
         if (error.response) {
            console.log(error.response);
            console.log(error.response.status);
            console.log(error.response.headers);
         }
      });
}

export default function Login() {
   const [username, setUsername] = useState('');
   const [email, setEmail] = useState('');
   const [password, setPassword] = useState('');

   const paperStyle = {
      padding: 20,
      height: '55vh',
      width: 310,
      margin: '20px auto',
   };
   const btnstyle = { margin: '8px 0' };
   return (
      <Grid>
         <Paper elevation={12} style={paperStyle}>
            <PersonIcon fontSize="large" />
            <h2>Sign In</h2>
            <TextField
               label="Username"
               placeholder="Enter Username"
               onChange={(event) => setUsername(event.target.value)}
               fullWidth
               required
            />
            <TextField
               label="Email"
               placeholder="Enter Email"
               onChange={(event) => setEmail(event.target.value)}
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
               onClick={() => sendData(username, email, password)}
               fullWidth
            >
               Sign in
            </Button>
            <Typography>
               <Link href="#">Forgot Password</Link>
            </Typography>
            <Typography>
               <Link href="#">Sign Up</Link>
            </Typography>
         </Paper>
      </Grid>
   );
}
