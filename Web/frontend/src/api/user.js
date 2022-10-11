import axios from "./index";
import {returnData} from "./utils";

export function getUser() {
    return axios.get(`/users/permissions/me`)
        .then(returnData)
}