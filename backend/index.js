const express  = require("express")
const app = express()
const http = require("http")
const server = http.createServer(app)
const socketIo = require("socket.io")(server, {cors: {origin: "*"}})
const PORT = process.env.PORT || 5000

app.use(express.urlencoded({extended: true}))
app.use(express.json())
app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', "*")
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE')
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type')
    res.setHeader('Access-Control-Allow-Credentials', true)
    next()
})

socketIo.on("connection",(socket) => {
	console.log("New client connected " + socket.id)
  
	socket.on("ClientToServer",(data)=> {
        console.log(data)
        const dataServer = {
            id:socket.id,
            content: "server"
        }
		socketIo.emit("ServerToClient", { dataServer })
	})
	socket.on("disconnect", () => {
	  console.log("Client disconnected " + socket.id)
	})
})

app.get('/',(req,res)=>{
    res.send("<h1>Server BTL Mạng máy tính</h1>")
})
server.listen(PORT, ()=>{
    console.log(`server is running on PORT ${PORT}`)
})