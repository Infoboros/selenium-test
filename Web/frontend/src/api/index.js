import Axios from "axios";

const axiosConfig = {
    baseURL: 'http://127.0.0.1/api',
    timeout: 30000,
    withCredentials: true
};
const axios = Axios.create(axiosConfig);

export default axios