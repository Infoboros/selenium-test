import {getEvents} from "../api/events";


const state = () => ({
    events: []
})

const getters = {

    events(state){
        return state.events
    }

}

const actions = {
    update({commit}) {
        return new Promise((resolve, reject) => {
            getEvents()
                .then(events => resolve(commit('update', events)))
                .catch(err => reject(err))
        })
    }
}


// mutations
const mutations = {
    update(state, events) {
        state.events = [...events]
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}