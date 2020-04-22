import React, { Component } from 'react';

import Dashboard from './todos/dashboard';
import { Provider } from 'react-redux';
import store from '../store';

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Dashboard />
            </Provider>
        )
    }
}

export default App;