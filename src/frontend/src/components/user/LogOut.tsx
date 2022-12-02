import axios from 'axios';

export function logout() {
   axios({
      url: 'http://127.0.0.1:5000/logout',
      withCredentials: true,
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
