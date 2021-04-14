import React from 'react'

const ToDolist = (props) => {


    return (
        <>
            <li>{props.text}</li>
            <button onClick={() => {
                props.onSelect(props.id)
            }}>Delete</button>
        </>
    )
}
export default ToDolist