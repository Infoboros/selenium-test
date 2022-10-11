import {getUser} from "../api/user";


const state = () => ({
    userData: {
        id: '',
        nick_name: '',
        id_name: '',
        avatar_url: '',
        date_registration: ''
    }
})

const getters = {

    userData(state){
        return state.userData
    }

}

const actions = {
    update({commit}) {
        return new Promise((resolve, reject) => {
            getUser()
                .then(userData => resolve(commit('update', userData)))
                .catch(err => reject(err))
        })
    }
}


// mutations
const mutations = {
    update(state, userData) {
        const avatar = userData.avatar

        state.userData = {
            ...userData,
            avatar: avatar ? avatar.url : ''
        }
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}