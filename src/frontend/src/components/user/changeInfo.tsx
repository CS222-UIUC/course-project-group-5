import axios from 'axios';

const baseURL = 'http://127.0.0.1:5000/user';

export function changeEmail(new_email: string, username: string) {
   const req = {
      is_email: true,
      email: new_email,
   };
   const json = JSON.stringify(req);
   axios({
      method: 'POST',
      url: `${baseURL}`,
      data: json,
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

export function changePhone(new_phone: string, username: string) {
   const req = {
      is_phone: true,
      phone: new_phone,
   };
   const json = JSON.stringify(req);
   axios({
      method: 'POST',
      url: `${baseURL}`,
      data: json,
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

export function logout() {
   axios({
      url: 'http://127.0.0.1:5000/logout',
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
