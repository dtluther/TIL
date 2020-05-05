import React, { Component } from 'react';
import { Provider } from 'react-redux';
import store from '../store';
import { Router, Route, Switch } from 'react-router-dom';

import Dashboard from './todos/dashboard';
import Header from './layout/header';
import history from '../history';
import TodoDelete from './todos/todo_delete';

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Router history={history}>
                    <Header />
                    <Switch>
                        <Route exact path='/' component={Dashboard} />
                        <Route exact path='/delete/:id' component={TodoDelete} />
                    </Switch>
                </Router>
            </Provider>
        )
    }
}

export default App;