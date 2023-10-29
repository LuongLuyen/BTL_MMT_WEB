import Home from './Home';
import Login from './Login';
import Transaction from './Transaction'
import{
  BrowserRouter as Router,
  Routes,
  Route,
} from 'react-router-dom'
function App() {
  return (
    <Router>
    <Routes>
      <Route path='/' element={<Home/>}/>
      <Route path='/login' element={<Login />}/>
      <Route path='/transaction' element={<Transaction />}/>
    </Routes>
  </Router>
  );
}

export default App;
