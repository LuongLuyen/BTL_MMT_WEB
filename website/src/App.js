import './App.css';
import React, { useState, useEffect, useRef } from "react"
import socketIOClient from "socket.io-client"

function App() {
  const socketRef = useRef()
  useEffect(() => {
    socketRef.current = socketIOClient.connect("http://localhost:5000")
    socketRef.current.on('ServerToClient', data => {
      console.log(data)
    })
    return () => {
      socketRef.current.disconnect()
    }
  }, [])
  const send = () => {
    const data = {
      id:1,
      content: "client"
    }
    socketRef.current.emit('ClientToServer', data)
  }
  return (
    <div className="App">
      <h1>Client BTL Mạng máy tính</h1>
      <div onClick={send}>btn</div>
    </div>
  );
}

export default App;
