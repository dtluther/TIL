import _ from 'lodash';
import { GET_TODOS } from '../actions/types';

export default (state = {}, action) => {
    // Object.freeze(state); # app academy way
    // let nextState = {};

    switch(action.type) {
        case GET_TODOS:
            return {
                ...state,
                ..._.mapKeys(action.payload, 'id')
            };
        default:
            return state;
    };
};