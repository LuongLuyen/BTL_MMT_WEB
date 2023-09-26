import React, {useEffect, useRef,useState } from "react"
import socketIOClient from "socket.io-client"
function App() {
  const [data, setData] = useState([])
  const [name, setName] = useState('')
  const [input, setInput] = useState('')
  const socketRef = useRef()
  
  useEffect(() => {
    socketRef.current = socketIOClient.connect("http://localhost:5000")
    return () => {
      socketRef.current.disconnect()
    }
  }, [])
  const Login = ()=>{
    const name = prompt("Nhập tên ?")
    setName(name)
  }
  const send = () => {
    if(name === ""){
      Login()
    }else{
      socketRef.current.emit('ClientToServer',{
        name:name,
        content: input
      })
      socketRef.current.on('ServerToClient', data => {
        setData(data)
      })
    }
  }

  return (
    <div className="Main">
      <h1>Client BTL Mạng máy tính</h1>
      <div>Đây là: {name}</div>
            <div>
              {data.map((item,index)=>(
                <div key={index}>
                  <span>Name:  {item.name}</span>
                  <br/>
                  <span>Message:   {item.content}</span>
                  <br/>
                  <br/>
                </div>
              ))}
            </div>
          <input value={input} onChange={(e)=>{setInput(e.target.value)}}/>
          <div onClick={send}>GỬI</div>
    </div>
  );
}

export default App;
