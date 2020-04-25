import React, { Component } from 'react';
import { connect } from 'react-redux';
import { addTodo } from '../../actions/todos';
import TodoForm from './todo_form';

class TodoCreate extends Component {
    onSubmit = formValues => {
        this.props.addTodo(formValues);
    };

    render() {
        return (
            <div style={{ marginTop: '2rem' }}>
                <TodoForm destroyOnUnmount={false} onSubmit={this.onSubmit} />
            </div>
        );
    };
};

export default connect(
    null, // when we don't need to specify a mapStateToProps
    { addTodo }
)(TodoCreate);