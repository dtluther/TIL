import axios from 'axios';
import { reset } from 'redux-form';
import { GET_TODOS, ADD_TODO, GET_TODO, DELETE_TODO } from './types';

// GET TODOS
export const getTodos = () => async dispatch => {
    const res = await axios.get('/api/todos/');
    dispatch({
        type: GET_TODOS,
        payload: res.data
    });
};

// ADD TODO
export const addTodo = formValues => async dispatch => {
    const res = await axios.get('/api/todos/', { ...formValues });
    dispatch({
        type: ADD_TODO,
        payload: res.data
    });
    dispatch(reset('todoForm')); // this clears the form after submission succeeeds
};

// GET TODO
export const getTodo = id => async dispatch => {
    const res = await axios.get(`/api/todos/${id}/`);
    dispatch({
        type: GET_TODO,
        payload: res.data
    });
};

// DELETE TODO
export const deleteTodo = id => async dispatch => {
    await axios.delete(`/api/todos/${id}/`);
    dispatch({
        type: DELETE_TODO,
        payload: id
    });
    history.push('/')
};