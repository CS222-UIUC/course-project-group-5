import { useEffect, useState } from 'react';
import axios from 'axios';
import { UserType } from '../Types';

const baseURL = 'http://127.0.0.1:5000/user';

function getInfo(username: string) {
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(false);
    const [user, setUser] = useState(defaultUser);

    useEffect(() => {
        //Gets user info on load
        setLoading(true);
        setError(false);
        const CancelToken = axios.CancelToken;
        const source = CancelToken.source();
        const timer = setTimeout(() => {
            axios({
                method: 'GET',
                url: `${baseURL}/${username}`,
                cancelToken: source.token,
             })
                .then((res) => {
                    setUser(() => {
                        return {
                            user_id: res.data.user_id,
                            username: res.data.username,
                            password: res.data.password,
                            email: res.data.email,
                            phone: res.data.phone,
                        }
                    })
                })
                .catch((e) => {
                    if (axios.isCancel(e)) return;
                    setError(true);
                });
        }, 700);
        return () => {
            clearTimeout(timer);
            source.cancel();
        };
    });
    return {loading, error, user};
}

function defaultUser(): UserType {
    // Default user for when page loads
    return {
        user_id: 0,
        username: "",
        password: "",
        email: "",
        phone: "",
    }
}