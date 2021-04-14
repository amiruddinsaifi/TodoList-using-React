import './App.css';
import React, { useState } from 'react';
import ToDolist from './ToDoList';

const App = () => {
  const [inputList, setInputList] = useState(" ");
  const [Items, setItems] = useState([]);

  const itemEvent = (event) => {
    setInputList(event.target.value)
  }
  const listOfItem = () => {
    setItems((oldItem) => {
      return [...oldItem, inputList]
    })
  }
  const deleteItems = (id) => {
    console.log('deleted')

    setItems((oldItem) => {
      return oldItem.filter((arrElem, index) => {
        return index !== id;
      })
    })
}
  return (
    <>
      <div className="main_div">
        <div className="center_div">
          <br />
          <h1>ToDo List</h1>
          <br />
          <input type="text" placeholder="Add item" onChange={itemEvent} value={inputList} />
          <button onClick={listOfItem}>add</button>
          {Items.map((itemval,index) => {
            return <ToDolist key={index}text={itemval} id={index} onSelect={deleteItems}></ToDolist>
          })}


        </div>
      </div>
    </>
  );
}

export default App;
