const express  = require("express")
const app = express()
const http = require("http")
const server = http.createServer(app)
const socketIo = require("socket.io")(server, {cors: {origin: "*"}})
const PORT = process.env.PORT || 5000
const ip = require("ip")

app.use(express.urlencoded({extended: true}))
app.use(express.json())
app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', "*")
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE')
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type')
    res.setHeader('Access-Control-Allow-Credentials', true)
    next()
})
const DB = []
socketIo.on("connection",(socket) => {
	console.log("Kết nối CLIENT thành công")
	socket.on("ClientToServer",(data)=> {
        console.log("Người dùng: ",data.name)
        console.log(data)
        DB.push(data)
        socketIo.emit("ServerToClient", DB)
	})
	socket.on("disconnect", () => {
	  console.log("Ngắt kết nối CLIENT")
      console.log("<<----------------------------------------->>")
	})
})

app.get('/',(req,res)=>{
    res.send("<h1>Server BTL Mạng máy tính</h1>")
})
server.listen(PORT, ()=>{
    console.log(`server is running ${ ip.address()}:${PORT}`)
})