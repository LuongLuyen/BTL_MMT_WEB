import React, {useEffect, useRef,useState } from "react"
import socketIOClient from "socket.io-client"
import './css/Phone.css'
function Home() {
  const [data, setData] = useState([])
  const [name, setName] = useState('')
  const [input, setInput] = useState('')
  const socketRef = useRef()
  
  useEffect(() => {
    socketRef.current = socketIOClient.connect("192.168.1.25:5000")
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
    <div className='app'>
      <div className="phone">
        <div className="phone__header">.</div>
        <div className="phone__main">
        <div className="Main">
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
              <br/>
              <br/>
              <button onClick={send}>GỬI</button>
          </div>
        </div>
        <div className="phone__footer"></div>
      </div>
    </div>   
  );
}

export default Home;