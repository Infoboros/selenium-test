import {twit} from "../api/feed";

const state = () => ({
    feed: []
})

const getters = {
    feed(state) {
        return state.feed
    },
}

const actions = {
    updateFeed({commit}, getFeed) {
        return new Promise((resolve, reject) => {
            getFeed()
                .then(feed => {
                    commit('updateFeed', feed)
                    resolve(feed)
                })
                .catch(err => reject(err))
        })
    },
    makeEvent({commit}, {twitId, userId, make, description}) {
        return new Promise((resolve, reject) => {
            make(twitId)
                .then(() => {
                    commit('makeEvent', {twit: twitId, user: userId, description: description})
                    resolve()
                })
                .catch(err => reject(err))
        })
    },
    makeTwit({commit}, text) {
        return new Promise((resolve, reject) => {
            twit(text)
                .then(twitInfo => {
                    commit('makeTwit', twitInfo)
                    resolve()
                })
                .catch(err => reject(err))
        })
    }

}


// mutations
const mutations = {
    updateFeed(state, feed) {
        state.feed = [...feed]
    },
    makeEvent(state, event) {
        const {
            twit,
            user,
            description
        } = event
        const newFeed = [...state.feed]

        const twitForEvent = newFeed.find(twitFromFeed => twitFromFeed.id === twit)

        const existsEvents = twitForEvent.event
            .filter(event => event.initiator.id === user && event.type.description === description)

        if (existsEvents.length)
            twitForEvent.event = twitForEvent.event.filter(event => {
                if (event.type.description !== description)
                    return true
                return event.initiator.id !== user
            })
        else
            twitForEvent.event.push({
                initiator: {
                    id: user
                },
                type: {
                    description: description
                }
            })

        state.feed = newFeed

    },
    makeTwit(state, twit) {
        state.feed = [twit, ...state.feed]
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}