import React from 'react';
import { Grid, Paper, Avatar, TextField, Button, Typography, Link, FormControlLabel, Checkbox } from '@mui/material';
import PersonIcon from '@mui/icons-material/Person';

export default function Login() {

  const paperStyle = { padding: 20, height: '70vh', width: 310, margin: "20px auto" }
  const avatarStyle = { backgroundColor: '#1bbd7e' }
  const btnstyle = { margin: '8px 0' }
  return (
    <Grid>
      <Paper elevation={12} style={paperStyle}>
        <PersonIcon fontSize="large" />
        <h2>Sign In</h2>
        <TextField label='Username' placeholder='Enter username' fullWidth required />
        <TextField label='Email' placeholder='Enter Email' fullWidth required />
        <TextField label='Password' placeholder='Enter Password' type='password' fullWidth required />

        <FormControlLabel
          control={
            <Checkbox
              name="checkedB"
              color="primary"
            />
          }
          label="Remember me"
        />
        <Button type='submit' color="primary" variant="contained" style={btnstyle} fullWidth>Sign in</Button>
        <Typography >
          <Link href="#" >
            Forgot Password
          </Link>
        </Typography>
        <Typography >
          <Link href="#" >
            Sign Up
          </Link>
        </Typography>
      </Paper>
    </Grid>
  )
}


