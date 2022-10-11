import {login, getUserId, register} from "../api/auth";


const state = () => ({
    userId: ''
})

const getters = {}

const actions = {
    getUserId({commit}){
        return new Promise((resolve, reject) => {
            getUserId()
                .then(userId => {
                    commit('auth_success', userId)
                })
                .catch(err => reject(err))

        })
    },
    login({dispatch}, user) {
        return new Promise((resolve, reject) => {
            login(user)
                .then(() => {
                    dispatch('getUserId')
                    resolve()
                })
                .catch(err => {
                    reject(err)
                })
        })
    },
    register({dispatch}, user) {
        return new Promise((resolve, reject) => {
            register(user)
                .then(() => {
                    dispatch('getUserId')
                    resolve()
                })
                .catch(err => {
                    reject(err)
                })
        })
    },
}


// mutations
const mutations = {
    auth_success(state, userId) {
        state.userId = userId
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}