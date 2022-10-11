import axios from "./index";

const baseAuthURL = '/users'

export function login({username, password}) {
    const bodyFormData = new FormData();

    bodyFormData.append('username', username)
    bodyFormData.append('password', password)

    return axios.post(`${baseAuthURL}/auth/login`, bodyFormData)
}

export function getUserId() {
    return axios.get(`${baseAuthURL}/permissions/me`)
        .then(response => response.data.id)
}

export function register(userData) {
    return axios.post(`${baseAuthURL}/auth/register`, userData)
}