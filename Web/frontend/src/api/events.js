import axios from "./index";
import {returnData} from "./utils";

const baseUrl = '/events/events'

export function repost(twitId) {
    return axios.put(`${baseUrl}/repost`, {twit_id: twitId})
        .then(returnData)
}


export function like(twitId) {
    return axios.put(`${baseUrl}/like`, {twit_id: twitId})
        .then(returnData)
}

export function getEvents() {
    return axios.get(`${baseUrl}/feed`)
        .then(returnData)
}