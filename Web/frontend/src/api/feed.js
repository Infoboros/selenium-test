import axios from "./index";
import {returnData} from "./utils";

const baseUrl = '/twits'

export function getProfileFeed() {
    return axios.get(`${baseUrl}/profile_feed`)
        .then(returnData)
}


export function getAllFeed() {
    return axios.get(`${baseUrl}/feed`)
        .then(returnData)
}

export function twit(text) {
    return axios.post(`${baseUrl}/`, {text: text})
        .then(returnData)
}